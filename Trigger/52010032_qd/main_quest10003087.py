""" trigger/52010032_qd/main_quest10003087.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003086,10003087], questStates=[2]):
            return NpcSpawn()


class NpcSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[601], arg2=True)
        create_monster(spawnIds=[602], arg2=True)
        set_npc_emotion_sequence(spawnId=601, sequenceName='Idle_A')
        set_npc_emotion_sequence(spawnId=602, sequenceName='Idle_A')


