""" trigger/52010032_qd/main_quest10003106.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003106], questStates=[1]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=2001, type='trigger', achieve='NewChief')


initial_state = idle
