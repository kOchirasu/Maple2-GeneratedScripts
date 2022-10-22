""" trigger/52020024_qd/52020024_timer.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='TimerStart', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5, clearAtZero=True, display=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='TimerStart', value=2)
        set_user_value(triggerId=99990003, key='FinalPhase', value=2)
        reset_timer(timerId='1')


