""" trigger/52020021_qd/main.xml """
import trigger_api


# 트로이 여관 216호실 : 52020020
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003073], questStates=[1]):
            return idle(self.ctx)


initial_state = idle
