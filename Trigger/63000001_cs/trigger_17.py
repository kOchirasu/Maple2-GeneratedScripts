""" trigger/63000001_cs/trigger_17.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[317], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[117]):
            return 발판17()


class 발판17(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[317], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[117]):
            return 발판17끝()


class 발판17끝(state.State):
    def on_enter(self):
        set_timer(timerId='417', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='417'):
            return 대기()


