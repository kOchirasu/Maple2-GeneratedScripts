""" trigger/63000001_cs/trigger_12.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[312], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[112]):
            return 발판12()


class 발판12(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[312], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[112]):
            return 발판12끝()


class 발판12끝(state.State):
    def on_enter(self):
        set_timer(timerId='412', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='412'):
            return 대기()


