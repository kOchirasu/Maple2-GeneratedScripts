""" trigger/63000001_cs/trigger_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[303], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 발판03()


class 발판03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[303], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[103]):
            return 발판03끝()


class 발판03끝(state.State):
    def on_enter(self):
        set_timer(timerId='403', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='403'):
            return 대기()


