""" trigger/63000001_cs/trigger_15.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[315], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[115]):
            return 발판15()


class 발판15(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[315], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[115]):
            return 발판15끝()


class 발판15끝(state.State):
    def on_enter(self):
        set_timer(timerId='415', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='415'):
            return 대기()


