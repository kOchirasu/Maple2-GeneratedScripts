""" trigger/52010023_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_effect(triggerIds=[7001], visible=False)
        create_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002500], questStates=[2]):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52010023_QD__MAIN__0$', arg4=5)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[101]):
            return Npc_out()


class Npc_out(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=True)
        destroy_monster(spawnIds=[101])


