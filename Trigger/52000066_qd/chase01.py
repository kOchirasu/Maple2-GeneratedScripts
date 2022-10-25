""" trigger/52000066_qd/chase01.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[1000], visible=False, animationEffect=False) # LadderEnterance
        self.set_ladder(triggerIds=[1001], visible=False, animationEffect=False) # LadderEnterance
        self.set_ladder(triggerIds=[1002], visible=False, animationEffect=False) # LadderEnterance
        self.set_ladder(triggerIds=[1003], visible=False, animationEffect=False) # LadderEnterance
        self.set_ladder(triggerIds=[1004], visible=False, animationEffect=False) # LadderEnterance
        self.set_ladder(triggerIds=[1005], visible=False, animationEffect=False) # LadderEnterance
        self.set_actor(triggerId=4000, visible=True, initialSequence='Closed') # TrapLever
        self.set_mesh(triggerIds=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], visible=True, arg3=0, delay=0, scale=3) # TrapMesh
        self.set_effect(triggerIds=[5001], visible=False) # DownArrow
        self.set_breakable(triggerIds=[4100], enable=False) # Move_Agent
        self.set_breakable(triggerIds=[4200], enable=False) # Move_Train
        self.set_visible_breakable_object(triggerIds=[4100], visible=False) # Move_Agent
        self.set_visible_breakable_object(triggerIds=[4200], visible=False) # Move_Train
        self.set_portal(portalId=2, visible=True, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return LodingDelay01(self.ctx)


class LodingDelay01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCMonologue01(self.ctx)


class PCMonologue01(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1002')
        self.set_conversation(type=1, spawnId=0, script='$52000066_QD__CHASE01__0$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return LodingDelay02(self.ctx)


class LodingDelay02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstCameraGuide01(self.ctx)


class FirstCameraGuide01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FirstCameraGuide02(self.ctx)


class FirstCameraGuide02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=600, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstPhaseChase01(self.ctx)


class FirstPhaseChase01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000066_QD__CHASE01__1$', arg3='3000', arg4='0')
        self.set_ladder(triggerIds=[1000], visible=True, animationEffect=True) # LadderEnterance
        self.set_ladder(triggerIds=[1001], visible=True, animationEffect=True) # LadderEnterance
        self.set_ladder(triggerIds=[1002], visible=True, animationEffect=True) # LadderEnterance
        self.set_ladder(triggerIds=[1003], visible=True, animationEffect=True) # LadderEnterance
        self.set_ladder(triggerIds=[1004], visible=True, animationEffect=True) # LadderEnterance
        self.set_ladder(triggerIds=[1005], visible=True, animationEffect=True) # LadderEnterance

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9200]):
            return SecondCameraGuide01(self.ctx)


class SecondCameraGuide01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=601, enable=True)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return SecondCameraGuide02(self.ctx)


class SecondCameraGuide02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000066, portalId=40)
        self.set_actor(triggerId=4000, visible=True, initialSequence='Opened') # TrapLever
        self.set_mesh(triggerIds=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], visible=False, arg3=500, delay=50, scale=1) # TrapMesh

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return SecondCameraGuide03(self.ctx)


class SecondCameraGuide03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=601, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return SecondPhaseChase01(self.ctx)


class SecondPhaseChase01(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1001')
        self.set_conversation(type=1, spawnId=0, script='$52000066_QD__CHASE01__2$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return SecondPhaseChase02(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class SecondPhaseChase02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])
        self.set_user_value(triggerId=2, key='TrapLeverOn', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25200661, textId=25200661, duration=6000) # 가이드 : 함정을 뛰어 넘거나 레버를 당겨 보세요.

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9300]):
            return ThirdPhaseChase01(self.ctx)


class ThirdPhaseChase01(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25200662, textId=25200662) # 가이드 : 발판을 타고 위로 올라가세요.

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9400,9401,9402,9403,9404,9405,9406]):
            return ThirdCameraGuide01(self.ctx)


# 범인이 수레타고 도망가는 연출
class ThirdCameraGuide01(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2, key='TrapLeverOn', value=2)
        self.hide_guide_summary(entityId=25200662)
        self.set_breakable(triggerIds=[4100], enable=True) # Move_Agent
        self.set_breakable(triggerIds=[4200], enable=True) # Move_Train
        self.set_visible_breakable_object(triggerIds=[4100], visible=True) # Move_Agent
        self.set_visible_breakable_object(triggerIds=[4200], visible=True) # Move_Train

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return ThirdCameraGuide02(self.ctx)


class ThirdCameraGuide02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=602, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ThirdCameraGuide03(self.ctx)

    def on_exit(self):
        self.move_user(mapId=52000066, portalId=30)


class ThirdCameraGuide03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=604, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCMonologue10(self.ctx)


class PCMonologue10(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000066_QD__CHASE01__3$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return FourthTrainMove01(self.ctx)

    def on_exit(self):
        self.select_camera(triggerId=604, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class FourthTrainMove01(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[4100], enable=False) # Move_Agent
        self.set_breakable(triggerIds=[4200], enable=False) # Move_Train
        self.set_visible_breakable_object(triggerIds=[4100], visible=False) # Move_Agent
        self.set_visible_breakable_object(triggerIds=[4200], visible=False) # Move_Train
        self.set_user_value(triggerId=3, key='TrainMove', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9500,9501,9502]):
            return AgentEscape01(self.ctx)


class AgentEscape01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_103')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return AgentEscape02(self.ctx)


class AgentEscape02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=603, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9600, spawnIds=[103]):
            return AgentEscape03(self.ctx)


class AgentEscape03(common.Trigger):
    def on_enter(self):
        self.create_item(spawnIds=[300], arg5=6000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return AgentEscape04(self.ctx)


class AgentEscape04(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103])
        self.select_camera(triggerId=603, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return PCMonologue20(self.ctx)


class PCMonologue20(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000066_QD__CHASE01__4$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return QuestEndCheck01(self.ctx)


class QuestEndCheck01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[10001028], questStates=[2]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=False)


initial_state = Wait
