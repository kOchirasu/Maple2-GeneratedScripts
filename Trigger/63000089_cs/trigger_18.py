""" trigger/63000089_cs/trigger_18.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[318], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[118]):
            return 발판18()


class 발판18(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[318], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[118]):
            return 발판18끝()


class 발판18끝(state.State):
    def on_enter(self):
        set_timer(timerId='418', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='418'):
            return 대기()


