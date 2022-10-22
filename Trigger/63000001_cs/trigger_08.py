""" trigger/63000001_cs/trigger_08.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[308], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[108]):
            return 발판08()


class 발판08(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[308], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[108]):
            return 발판08끝()


class 발판08끝(state.State):
    def on_enter(self):
        set_timer(timerId='408', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='408'):
            return 대기()


