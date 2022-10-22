""" trigger/52010032_qd/main_quest10003106.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003106], questStates=[1]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_achievement(triggerId=2001, type='trigger', achieve='NewChief')


