""" trigger/52000029_qd/npc.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[2001]):
            destroy_monster(spawnIds=[2001])
            return 종료()


class 종료(state.State):
    pass


