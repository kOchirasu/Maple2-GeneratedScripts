""" trigger/63000001_cs/trigger_14.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[314], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[114]):
            return 발판14()


class 발판14(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[314], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[114]):
            return 발판14끝()


class 발판14끝(state.State):
    def on_enter(self):
        set_timer(timerId='414', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='414'):
            return 대기()


