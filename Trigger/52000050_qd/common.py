""" trigger/52000050_qd/common.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[121]):
            return npc_exit_01()
        if npc_detected(boxId=702, spawnIds=[122]):
            return npc_exit_02()


class npc_exit_01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[121])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[122])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


