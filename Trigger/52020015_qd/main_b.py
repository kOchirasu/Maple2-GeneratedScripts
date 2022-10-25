""" trigger/52020015_qd/main_b.xml """
import common


class Idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[60200010], questStates=[1]):
            return Idle(self.ctx)


initial_state = Idle
