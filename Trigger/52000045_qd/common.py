""" trigger/52000045_qd/common.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[201]):
            return npc_exit_01()
        if npc_detected(boxId=702, spawnIds=[202]):
            return npc_exit_02()
        if npc_detected(boxId=702, spawnIds=[203]):
            return npc_exit_03()
        if npc_detected(boxId=702, spawnIds=[204]):
            return npc_exit_04()
        if npc_detected(boxId=702, spawnIds=[205]):
            return npc_exit_05()
        if npc_detected(boxId=702, spawnIds=[206]):
            return npc_exit_06()


class npc_exit_01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[203])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[204])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[205])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_06(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[206])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


