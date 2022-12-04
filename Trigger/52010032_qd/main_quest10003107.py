""" trigger/52010032_qd/main_quest10003107.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003105,10003106], questStates=[2]):
            return NpcSpawn_01(self.ctx)


class NpcSpawn_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[502], animationEffect=True)
        self.set_npc_emotion_sequence(spawnId=502, sequenceName='Idle_A')


initial_state = Ready
