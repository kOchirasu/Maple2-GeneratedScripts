""" trigger/52000014_qd/meteo_3000.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 낙하01()


class 낙하01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 초기화()


class 초기화(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 낙하01()


