""" trigger/52100107_qd/main.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[91000890], questStates=[3]):
            return NPC소환()
        if quest_user_detected(boxIds=[9001], questIds=[91000900], questStates=[1]):
            return NPC소환()
        if quest_user_detected(boxIds=[9001], questIds=[91000900], questStates=[2]):
            return NPC소환()


class NPC소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)


