""" trigger/52100107_qd/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[91000890], questStates=[3]):
            return NPC소환(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000900], questStates=[1]):
            return NPC소환(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000900], questStates=[2]):
            return NPC소환(self.ctx)


class NPC소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=False)


initial_state = Ready
