""" trigger/63000001_cs/trigger_16.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[316], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[116]):
            return 발판16()


class 발판16(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[316], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[116]):
            return 발판16끝()


class 발판16끝(state.State):
    def on_enter(self):
        set_timer(timerId='416', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='416'):
            return 대기()


