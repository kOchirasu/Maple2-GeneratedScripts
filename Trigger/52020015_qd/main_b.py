""" trigger/52020015_qd/main_b.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[60200010], questStates=[1]):
            return Idle()


