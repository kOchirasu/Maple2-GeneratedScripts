""" trigger/99999905/score02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000414], arg2=0):
            return 점수()


class 점수(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[604], visible=True) # action name="전장점수를준다" arg1="105" arg2="50" /

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


