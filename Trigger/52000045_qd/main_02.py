""" trigger/52000045_qd/main_02.xml """
from common import *
import state


class ready(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701], jobCode=100):
            set_actor(triggerId=5001, visible=False, initialSequence='Idle_A')
            set_actor(triggerId=5002, visible=False, initialSequence='Idle_A')
            set_actor(triggerId=5003, visible=False, initialSequence='Idle_A')
            return ready_02()


class ready_02(state.State):
    def on_enter(self):
        move_user(mapId=52000045, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return start()


class start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[902], arg2=False) # 로스트차일드
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user_path(patrolName='MS2PatrolData_2010') # 유저를 이동시킨다
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        move_npc(spawnId=902, patrolName='MS2PatrolData_2004')
        move_user_path(patrolName='MS2PatrolData_2003') # 유저를 이동시킨다
        select_camera_path(pathIds=[8010], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return setup_userscript01()


class setup_userscript01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_02__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_A_03()


class start_A_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010,8013], returnView=False)
        set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_02__3$', arg4=3)
        set_conversation(type=1, spawnId=902, script='$52000045_QD__MAIN_02__4$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_03()


class start_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=902, script='$52000045_QD__MAIN_02__1$', arg4=3, arg5=1)
        set_npc_emotion_loop(spawnId=902, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_04()


class start_04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7003], visible=True)
        create_monster(spawnIds=[887,886,888], arg2=False)
        set_conversation(type=1, spawnId=902, script='$52000045_QD__MAIN_02__5$', arg4=1, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return start_05()


class start_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8014], returnView=False)
        set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_02__6$', arg4=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2200):
            return start_06()


class start_06(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Down2_A','Down_Idle_A','Down_Idle_A','Down_Idle_A','Down_Idle_A','Down_Idle_A'])
        set_effect(triggerIds=[7005], visible=True)
        set_effect(triggerIds=[7004], visible=True)
        create_monster(spawnIds=[872,873], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2050):
            return start_07()


class start_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8014,8015], returnView=False)
        create_monster(spawnIds=[871,876], arg2=False)
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=80000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=900):
            return start_08()


class start_08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[872,875,871,876], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start_09()


class start_09(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7005], visible=False)
        create_monster(spawnIds=[874,873,872], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return start_10()


class start_10(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return end()


class end(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='InvestgatedScretroom') # 퀘스트 목표 체크용 업적이벤트 발생
        move_user(mapId=52000046, portalId=1)


