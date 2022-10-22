""" trigger/52010032_qd/main_quest10003108.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003105,10003106,10003107], questStates=[2]):
            return NpcSpawn_02()


class NpcSpawn_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[501], arg2=True)
        set_npc_emotion_sequence(spawnId=501, sequenceName='Idle_A')


