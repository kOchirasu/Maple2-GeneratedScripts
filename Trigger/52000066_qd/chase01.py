""" trigger/52000066_qd/chase01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[1000], visible=False, animationEffect=False) # LadderEnterance
        set_ladder(triggerIds=[1001], visible=False, animationEffect=False) # LadderEnterance
        set_ladder(triggerIds=[1002], visible=False, animationEffect=False) # LadderEnterance
        set_ladder(triggerIds=[1003], visible=False, animationEffect=False) # LadderEnterance
        set_ladder(triggerIds=[1004], visible=False, animationEffect=False) # LadderEnterance
        set_ladder(triggerIds=[1005], visible=False, animationEffect=False) # LadderEnterance
        set_actor(triggerId=4000, visible=True, initialSequence='Closed') # TrapLever
        set_mesh(triggerIds=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], visible=True, arg3=0, arg4=0, arg5=3) # TrapMesh
        set_effect(triggerIds=[5001], visible=False) # DownArrow
        set_breakable(triggerIds=[4100], enabled=False) # Move_Agent
        set_breakable(triggerIds=[4200], enabled=False) # Move_Train
        set_visible_breakable_object(triggerIds=[4100], arg2=False) # Move_Agent
        set_visible_breakable_object(triggerIds=[4200], arg2=False) # Move_Train
        set_portal(portalId=2, visible=True, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if check_user():
            return LodingDelay01()


class LodingDelay01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCMonologue01()


class PCMonologue01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1002')
        set_conversation(type=1, spawnId=0, script='$52000066_QD__CHASE01__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return LodingDelay02()


class LodingDelay02(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstCameraGuide01()


class FirstCameraGuide01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FirstCameraGuide02()


class FirstCameraGuide02(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstPhaseChase01()


class FirstPhaseChase01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52000066_QD__CHASE01__1$', arg3='3000', arg4='0')
        set_ladder(triggerIds=[1000], visible=True, animationEffect=True) # LadderEnterance
        set_ladder(triggerIds=[1001], visible=True, animationEffect=True) # LadderEnterance
        set_ladder(triggerIds=[1002], visible=True, animationEffect=True) # LadderEnterance
        set_ladder(triggerIds=[1003], visible=True, animationEffect=True) # LadderEnterance
        set_ladder(triggerIds=[1004], visible=True, animationEffect=True) # LadderEnterance
        set_ladder(triggerIds=[1005], visible=True, animationEffect=True) # LadderEnterance

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return SecondCameraGuide01()


class SecondCameraGuide01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=True)
        create_monster(spawnIds=[102], arg2=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return SecondCameraGuide02()


class SecondCameraGuide02(state.State):
    def on_enter(self):
        move_user(mapId=52000066, portalId=40)
        set_actor(triggerId=4000, visible=True, initialSequence='Opened') # TrapLever
        set_mesh(triggerIds=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], visible=False, arg3=500, arg4=50, arg5=1) # TrapMesh

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return SecondCameraGuide03()


class SecondCameraGuide03(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return SecondPhaseChase01()


class SecondPhaseChase01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1001')
        set_conversation(type=1, spawnId=0, script='$52000066_QD__CHASE01__2$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return SecondPhaseChase02()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class SecondPhaseChase02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        set_user_value(triggerId=2, key='TrapLeverOn', value=1)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25200661, textId=25200661, duration=6000) # 가이드 : 함정을 뛰어 넘거나 레버를 당겨 보세요.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9300]):
            return ThirdPhaseChase01()


class ThirdPhaseChase01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25200662, textId=25200662) # 가이드 : 발판을 타고 위로 올라가세요.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9400,9401,9402,9403,9404,9405,9406]):
            return ThirdCameraGuide01()


#  범인이 수레타고 도망가는 연출 
class ThirdCameraGuide01(state.State):
    def on_enter(self):
        set_user_value(triggerId=2, key='TrapLeverOn', value=2)
        hide_guide_summary(entityId=25200662)
        set_breakable(triggerIds=[4100], enabled=True) # Move_Agent
        set_breakable(triggerIds=[4200], enabled=True) # Move_Train
        set_visible_breakable_object(triggerIds=[4100], arg2=True) # Move_Agent
        set_visible_breakable_object(triggerIds=[4200], arg2=True) # Move_Train

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ThirdCameraGuide02()


class ThirdCameraGuide02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=602, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ThirdCameraGuide03()

    def on_exit(self):
        move_user(mapId=52000066, portalId=30)


class ThirdCameraGuide03(state.State):
    def on_enter(self):
        select_camera(triggerId=604, enable=True)
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCMonologue10()


class PCMonologue10(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000066_QD__CHASE01__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FourthTrainMove01()

    def on_exit(self):
        select_camera(triggerId=604, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class FourthTrainMove01(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4100], enabled=False) # Move_Agent
        set_breakable(triggerIds=[4200], enabled=False) # Move_Train
        set_visible_breakable_object(triggerIds=[4100], arg2=False) # Move_Agent
        set_visible_breakable_object(triggerIds=[4200], arg2=False) # Move_Train
        set_user_value(triggerId=3, key='TrainMove', value=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9500,9501,9502]):
            return AgentEscape01()


class AgentEscape01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_103')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return AgentEscape02()


class AgentEscape02(state.State):
    def on_enter(self):
        select_camera(triggerId=603, enable=True)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9600, spawnIds=[103]):
            return AgentEscape03()


class AgentEscape03(state.State):
    def on_enter(self):
        create_item(spawnIds=[300], arg5=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return AgentEscape04()


class AgentEscape04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])
        select_camera(triggerId=603, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PCMonologue20()


class PCMonologue20(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000066_QD__CHASE01__4$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return QuestEndCheck01()


class QuestEndCheck01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[10001028], questStates=[2]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=False)


