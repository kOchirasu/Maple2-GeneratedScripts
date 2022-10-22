""" trigger/52010012_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[1003,1004], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10002797], questStates=[1]):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103,104,105])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,104,105]):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[106])
        move_npc(spawnId=106, patrolName='MS2PatrolData_1001')
        set_conversation(type=1, spawnId=106, script='$52010012_QD__MAIN__0$', arg4=3)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_mesh(triggerIds=[1003,1004], visible=True, arg3=0, arg4=80, arg5=10)
        set_mesh(triggerIds=[1001,1002], visible=False, arg3=0, arg4=80, arg5=10)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return Event_04()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)
        select_camera(triggerId=8001, enable=False)


class Event_04(state.State):
    def on_enter(self):
        move_npc(spawnId=106, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[106]):
            return End()


class End(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        destroy_monster(spawnIds=[106])


