""" trigger/52000070_qd/npcdown_901.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9900, spawnIds=[901]):
            return NpcFight()


class NpcFight(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901]):
            return NpcDown()


class NpcDown(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301], arg2=False)


