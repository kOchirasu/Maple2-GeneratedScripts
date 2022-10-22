""" trigger/02000386_bf/main_02.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[901]):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=901, script='$02000386_BF__MAIN_02__0$', arg4=2, arg5=0)
        move_npc(spawnId=901, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return end()


class end(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[901])


