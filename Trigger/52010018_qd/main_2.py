""" trigger/52010018_qd/main_2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3003], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3004], visible=False, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=201, visible=False, initialSequence='Eff_MassiveEvent_Door_Vanished')
        set_actor(triggerId=202, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=203, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=204, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=205, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=206, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=207, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=208, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=209, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=210, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=211, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[100], questIds=[10002853], questStates=[1]):
            return 미카이동02()


class 미카이동02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=302, enable=True)
        destroy_monster(spawnIds=[1005])
        create_monster(spawnIds=[1007], arg2=False)
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1007_A')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=104, spawnIds=[1007]):
            return 다리생성대기()


class 다리생성대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3003], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3004], visible=True, arg3=0, arg4=0, arg5=0)
            return 다리생성()


class 다리생성(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_actor(triggerId=201, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')
            set_actor(triggerId=202, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            set_actor(triggerId=203, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            set_actor(triggerId=204, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            set_actor(triggerId=205, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            set_actor(triggerId=206, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            set_actor(triggerId=207, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            set_actor(triggerId=208, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            set_actor(triggerId=209, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            set_actor(triggerId=210, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            set_actor(triggerId=211, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            return 미카대사02()


class 미카대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010018_QD__MAIN_2__0$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 에레브대사02()


class 에레브대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52010018_QD__MAIN_2__1$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 미카대사03()


class 미카대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010018_QD__MAIN_2__2$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            move_npc(spawnId=1007, patrolName='MS2PatrolData_1007_B')
            return 미카소멸()


class 미카소멸(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            select_camera(triggerId=302, enable=False)
            destroy_monster(spawnIds=[1007])
            set_achievement(triggerId=100, type='trigger', achieve='BacktoDrakenheim')
            return 종료()


class 종료(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_actor(triggerId=201, visible=False, initialSequence='Eff_MassiveEvent_Door_Vanished')
            set_actor(triggerId=202, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            set_actor(triggerId=203, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            set_actor(triggerId=204, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            set_actor(triggerId=205, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            set_actor(triggerId=206, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            set_actor(triggerId=207, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            set_actor(triggerId=208, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            set_actor(triggerId=209, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            set_actor(triggerId=210, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            set_actor(triggerId=211, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            return 종료2()


class 종료2(state.State):
    pass


