""" trigger/52000028_qd/npc_1014.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[1014]):
            destroy_monster(spawnIds=[1014])
            return 종료()


class 종료(state.State):
    pass


