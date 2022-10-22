""" trigger/52000047_qd/npcdown_507.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9900, spawnIds=[907]):
            return NpcFight()


class NpcFight(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[907]):
            return NpcDown()


class NpcDown(state.State):
    def on_enter(self):
        create_monster(spawnIds=[517], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='NpcRemove', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[517])
        set_user_value(key='NpcRemove', value=0)


