""" trigger/52000066_qd/train03.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False) # DownArrow
        self.set_interact_object(triggerIds=[10001072], state=1) # TrainLever
        self.set_user_value(key='TrainMove', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TrainMove', value=1):
            return FourthPhaseChase01(self.ctx)

    def on_exit(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25200663, textId=25200663) # 가이드 : 레버를 당겨 보세요.


class FourthPhaseChase01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True) # DownArrow

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001072], stateValue=0):
            return FourthPhaseChase02(self.ctx)


class FourthPhaseChase02(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25200663)
        self.set_effect(triggerIds=[5001], visible=False) # DownArrow
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_200')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GetInTheTrain01(self.ctx)


class GetInTheTrain01(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25200664, textId=25200664) # 가이드 : 수레에 타세요.

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9700]):
            return GetInTheTrain02(self.ctx)


class GetInTheTrain02(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=700, enable=True) # LocalTargetCamera
        self.hide_guide_summary(entityId=25200664)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25200665, textId=25200665, duration=2000) # 가이드 : 출발합니다!

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return GetInTheTrain03(self.ctx)


class GetInTheTrain03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return GetInTheTrain04(self.ctx)


class GetInTheTrain04(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=700, enable=False) # LocalTargetCamera

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthPhaseChase01(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[5001], visible=True) # DownArrow
        self.set_interact_object(triggerIds=[10001072], state=1) # TrainLever


initial_state = Wait
