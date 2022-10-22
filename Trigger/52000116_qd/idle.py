""" trigger/52000116_qd/idle.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101]) # Nelf_11003163

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return nelftalk()


class nelftalk(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52000116_QD__IDLE__0$', arg4=3, arg5=0) # 넬프 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return nelfmove()


class nelfmove(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_3001')


