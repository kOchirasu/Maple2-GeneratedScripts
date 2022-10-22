""" trigger/52010032_qd/main_quest10003107.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003105,10003106], questStates=[2]):
            return NpcSpawn_01()


class NpcSpawn_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[502], arg2=True)
        set_npc_emotion_sequence(spawnId=502, sequenceName='Idle_A')


