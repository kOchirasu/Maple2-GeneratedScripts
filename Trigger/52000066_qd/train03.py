""" trigger/52000066_qd/train03.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False) # DownArrow
        set_interact_object(triggerIds=[10001072], state=1) # TrainLever
        set_user_value(key='TrainMove', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TrainMove', value=1):
            return FourthPhaseChase01()

    def on_exit(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25200663, textId=25200663) # 가이드 : 레버를 당겨 보세요.


class FourthPhaseChase01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # DownArrow

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001072], arg2=0):
            return FourthPhaseChase02()


class FourthPhaseChase02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25200663)
        set_effect(triggerIds=[5001], visible=False) # DownArrow
        create_monster(spawnIds=[201], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_200')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GetInTheTrain01()


class GetInTheTrain01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25200664, textId=25200664) # 가이드 : 수레에 타세요.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9700]):
            return GetInTheTrain02()


class GetInTheTrain02(state.State):
    def on_enter(self):
        set_local_camera(cameraId=700, enable=True) # LocalTargetCamera
        hide_guide_summary(entityId=25200664)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25200665, textId=25200665, duration=2000) # 가이드 : 출발합니다!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return GetInTheTrain03()


class GetInTheTrain03(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return GetInTheTrain04()


class GetInTheTrain04(state.State):
    def on_enter(self):
        set_local_camera(cameraId=700, enable=False) # LocalTargetCamera

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthPhaseChase01()

    def on_exit(self):
        set_effect(triggerIds=[5001], visible=True) # DownArrow
        set_interact_object(triggerIds=[10001072], state=1) # TrainLever


