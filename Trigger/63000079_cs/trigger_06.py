""" trigger/63000079_cs/trigger_06.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[306], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 발판06()


class 발판06(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[306], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[106]):
            return 발판06끝()


class 발판06끝(state.State):
    def on_enter(self):
        set_timer(timerId='406', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='406'):
            return 대기()


