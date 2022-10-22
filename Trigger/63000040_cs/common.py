""" trigger/63000040_cs/common.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[101]):
            return npc_exit_01()
        if npc_detected(boxId=702, spawnIds=[103]):
            return npc_exit_02()


class npc_exit_01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


