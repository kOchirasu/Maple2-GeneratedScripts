""" trigger/52000045_qd/common_02.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[301]):
            return npc_exit_01()
        if npc_detected(boxId=702, spawnIds=[302]):
            return npc_exit_02()
        if npc_detected(boxId=702, spawnIds=[303]):
            return npc_exit_03()
        if npc_detected(boxId=702, spawnIds=[304]):
            return npc_exit_04()
        if npc_detected(boxId=702, spawnIds=[305]):
            return npc_exit_05()
        if npc_detected(boxId=702, spawnIds=[306]):
            return npc_exit_06()


class npc_exit_01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[301])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[302])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[303])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[304])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[305])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


class npc_exit_06(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[306])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


