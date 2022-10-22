""" trigger/52000067_qd/sub_event_05.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=707, spawnIds=[751]):
            return NPC소멸751()
        if npc_detected(boxId=707, spawnIds=[752]):
            return NPC소멸752()
        if npc_detected(boxId=707, spawnIds=[753]):
            return NPC소멸753()
        if npc_detected(boxId=707, spawnIds=[754]):
            return NPC소멸754()
        if npc_detected(boxId=707, spawnIds=[755]):
            return NPC소멸755()
        if npc_detected(boxId=707, spawnIds=[756]):
            return NPC소멸756()
        if npc_detected(boxId=707, spawnIds=[757]):
            return NPC소멸757()
        if npc_detected(boxId=707, spawnIds=[758]):
            return NPC소멸758()
        if npc_detected(boxId=707, spawnIds=[759]):
            return NPC소멸759()
        if npc_detected(boxId=707, spawnIds=[761]):
            return NPC소멸761()
        if npc_detected(boxId=707, spawnIds=[762]):
            return NPC소멸762()
        if npc_detected(boxId=707, spawnIds=[591]):
            return NPC소멸591()
        if npc_detected(boxId=707, spawnIds=[592]):
            return NPC소멸592()


class NPC소멸751(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[751])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸752(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[752])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸753(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[753])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸754(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[754])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸755(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[755])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸756(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[756])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸757(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[757])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸758(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[758])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸759(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[759])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸761(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[761])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸762(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[762])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸591(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[591])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


class NPC소멸592(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[592])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return idle()


