""" trigger/63000079_cs/trigger_11.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[311], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[111]):
            return 발판11()


class 발판11(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[311], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[111]):
            return 발판11끝()


class 발판11끝(state.State):
    def on_enter(self):
        set_timer(timerId='411', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='411'):
            return 대기()


