""" trigger/02000348_bf/npc_move.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=60004, boxId=1):
            return start()


class start(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000348_BF__NPC_MOVE__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=60003, spawnIds=[102]):
            return end()
        if wait_tick(waitTick=2000):
            return end()


class end(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])


