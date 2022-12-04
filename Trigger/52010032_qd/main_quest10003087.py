""" trigger/52010032_qd/main_quest10003087.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003086,10003087], questStates=[2]):
            return NpcSpawn(self.ctx)


class NpcSpawn(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[601], animationEffect=True)
        self.create_monster(spawnIds=[602], animationEffect=True)
        self.set_npc_emotion_sequence(spawnId=601, sequenceName='Idle_A')
        self.set_npc_emotion_sequence(spawnId=602, sequenceName='Idle_A')


initial_state = Ready
