""" trigger/52020021_qd/main.xml """
from common import *
import state


#  트로이 여관 216호실 : 52020020  
class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003073], questStates=[1]):
            return idle()


