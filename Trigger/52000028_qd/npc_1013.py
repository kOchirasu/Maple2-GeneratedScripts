""" trigger/52000028_qd/npc_1013.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[1013]):
            destroy_monster(spawnIds=[1013])
            return 종료()


class 종료(state.State):
    pass


