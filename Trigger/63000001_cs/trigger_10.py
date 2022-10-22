""" trigger/63000001_cs/trigger_10.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[310], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[110]):
            return 발판10()


class 발판10(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[310], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[110]):
            return 발판10끝()


class 발판10끝(state.State):
    def on_enter(self):
        set_timer(timerId='410', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='410'):
            return 대기()


