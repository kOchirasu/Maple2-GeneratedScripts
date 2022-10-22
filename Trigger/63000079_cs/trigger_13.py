""" trigger/63000079_cs/trigger_13.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[313], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[113]):
            return 발판13()


class 발판13(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[313], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[113]):
            return 발판13끝()


class 발판13끝(state.State):
    def on_enter(self):
        set_timer(timerId='413', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='413'):
            return 대기()


