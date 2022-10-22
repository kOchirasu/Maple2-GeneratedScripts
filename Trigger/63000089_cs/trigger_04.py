""" trigger/63000089_cs/trigger_04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[304], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 발판04()


class 발판04(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[304], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[104]):
            return 발판04끝()


class 발판04끝(state.State):
    def on_enter(self):
        set_timer(timerId='404', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='404'):
            return 대기()


