""" trigger/52020039_qd/main.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[91000590], questStates=[3]):
            return NPC소환()
        if quest_user_detected(boxIds=[9001], questIds=[91000600], questStates=[1]):
            return NPC소환()
        if quest_user_detected(boxIds=[9001], questIds=[91000600], questStates=[2]):
            return NPC소환()


class NPC소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        create_monster(spawnIds=[107], arg2=False)
        create_monster(spawnIds=[108], arg2=False)
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[110], arg2=False)
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[112], arg2=False)
        create_monster(spawnIds=[113], arg2=False)
        create_monster(spawnIds=[114], arg2=False)
        create_monster(spawnIds=[115], arg2=False)
        create_monster(spawnIds=[116], arg2=False)
        create_monster(spawnIds=[117], arg2=False)
        create_monster(spawnIds=[118], arg2=False)
        create_monster(spawnIds=[119], arg2=False)
        create_monster(spawnIds=[120], arg2=False)


