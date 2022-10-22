""" trigger/63000089_cs/trigger_09.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[309], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[109]):
            return 발판09()


class 발판09(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[309], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[109]):
            return 발판09끝()


class 발판09끝(state.State):
    def on_enter(self):
        set_timer(timerId='409', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='409'):
            return 대기()


