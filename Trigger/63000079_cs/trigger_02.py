""" trigger/63000079_cs/trigger_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[302], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 발판02()


class 발판02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[302], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[102]):
            return 발판02끝()


class 발판02끝(state.State):
    def on_enter(self):
        set_timer(timerId='402', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='402'):
            return 대기()


