""" trigger/52000045_qd/main_01.xml """
from common import *
import state


class ready(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701], jobCode=110):
            set_effect(triggerIds=[7001], visible=True)
            return start()


class start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[101], arg2=False) # 비전
        add_buff(boxIds=[701], skillId=70000105, level=1) # 투명 버프를 걸어준다
        set_conversation(type=2, spawnId=11001560, script='$52000045_QD__MAIN_01__0$', arg4=5)
        create_monster(spawnIds=[201,202,203,204,205,206], arg2=False)
        create_monster(spawnIds=[301,302,303,304,305,306], arg2=False)
        create_monster(spawnIds=[401,402,403,404,405], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=201, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=202, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=203, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=204, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=205, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=206, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=301, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=302, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=303, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=304, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=305, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=306, patrolName='MS2PatrolData_2001')
        select_camera_path(pathIds=[8001,8002,8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_03()


class start_03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001560, script='$52000045_QD__MAIN_01__1$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            create_monster(spawnIds=[101], arg2=False)
            remove_buff(boxId=701, skillId=70000105)
            select_camera_path(pathIds=[8004], returnView=True)
            destroy_monster(spawnIds=[101])
            destroy_monster(spawnIds=[401,402,403,404,405])
            set_actor(triggerId=5001, visible=False, initialSequence='Idle_A')
            set_actor(triggerId=5002, visible=False, initialSequence='Idle_A')
            set_actor(triggerId=5003, visible=False, initialSequence='Idle_A')
            set_cinematic_ui(type=4)
            return start_04()


class start_04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_effect(triggerIds=[7001], visible=False)
            add_buff(boxIds=[701], skillId=70000094, level=1)
            set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=4000)
            set_cinematic_ui(type=1)
            set_cinematic_ui(type=3)
            return start_05()


class start_05(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            set_pc_emotion_sequence(sequenceNames=['Emotion_Failure_Idle_A'])
            return start_06()


class start_06(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_effect(triggerIds=[7002], visible=True)
            move_user_path(patrolName='MS2PatrolData_2002')
            return start_07()


class start_07(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start_08()


class start_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)
        create_monster(spawnIds=[901], arg2=False) # 스커
        move_user_path(patrolName='MS2PatrolData_2004') # 유저를 이동시킨다
        move_npc(spawnId=901, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_09()


class start_09(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=901, script='$52000045_QD__MAIN_01__2$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_A_10()


class start_A_10(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=901, script='$52000045_QD__MAIN_01__11$', arg4=3)
        set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_01__12$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_10()


class start_10(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_01__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            set_effect(triggerIds=[7003], visible=True)
            move_npc(spawnId=901, patrolName='MS2PatrolData_2005')
            return start_11()


class start_11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[801,802,803,804,805,806], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return start_12()


class start_12(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return start_13()


class start_13(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7004], visible=True)
        select_camera_path(pathIds=[8004], returnView=True)
        create_monster(spawnIds=[809], arg2=False)
        set_npc_emotion_loop(spawnId=901, sequenceName='Down_Idle_A', duration=300000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            show_guide_summary(entityId=25200473, textId=25200473)
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            return start_14()


class start_14(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[801,802,803,804,805,806,809]):
            hide_guide_summary(entityId=25200473)
            return start_15()


class start_15(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start_16()


class start_16(state.State):
    def on_enter(self):
        create_monster(spawnIds=[7701,7702], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            select_camera_path(pathIds=[8004], returnView=False)
            return start_17()


class start_17(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=7702, sequenceName='Talk_A', duration=3000)
        set_conversation(type=2, spawnId=11001545, script='$52000045_QD__MAIN_01__4$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_18()


class start_18(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=7701, sequenceName='Talk_A', duration=3000)
        set_conversation(type=2, spawnId=11001546, script='$52000045_QD__MAIN_01__5$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            move_user_path(patrolName='MS2PatrolData_2006')
            move_npc(spawnId=7701, patrolName='MS2PatrolData_7003')
            move_npc(spawnId=7702, patrolName='MS2PatrolData_7004')
            return start_19()


class start_19(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            select_camera_path(pathIds=[8005], returnView=False)
            return start_20()


class start_20(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=7701, script='$52000045_QD__MAIN_01__6$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=7702, script='$52000045_QD__MAIN_01__7$', arg4=3, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_21()


class start_21(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_01__8$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_01__9$', arg4=3, arg5=2)
        set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_01__10$', arg4=3, arg5=6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return start_22()


class start_22(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2007') # 유저를 이동시킨다

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_achievement(triggerId=701, type='trigger', achieve='MeetAgainStriker')
            move_user(mapId=2000138, portalId=103)
            return start_22()


