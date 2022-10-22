""" trigger/52010009_qd/npc_out.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[111]):
            return npc_out()
        if npc_detected(boxId=702, spawnIds=[112]):
            return npc_out()
        if npc_detected(boxId=702, spawnIds=[113]):
            return npc_out()


class npc_out(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111,112,113])

    def on_tick(self) -> state.State:
        if true():
            return idle()


