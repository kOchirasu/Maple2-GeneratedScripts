""" trigger/63000089_cs/trigger_07.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[307], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[107]):
            return 발판07()


class 발판07(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[307], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[107]):
            return 발판07끝()


class 발판07끝(state.State):
    def on_enter(self):
        set_timer(timerId='407', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='407'):
            return 대기()


