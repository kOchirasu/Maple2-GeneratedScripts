""" trigger/52020021_qd/main.xml """
import common


# 트로이 여관 216호실 : 52020020
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003073], questStates=[1]):
            return idle(self.ctx)


initial_state = idle
