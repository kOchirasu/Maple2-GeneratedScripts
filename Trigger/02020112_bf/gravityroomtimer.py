""" trigger/02020112_bf/gravityroomtimer.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990020, key='TimerReset', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Timer', value=1):
            return 타이머시작()


class 타이머시작(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10, clearAtZero=True, display=True, arg5=-40)

    def on_tick(self) -> state.State:
        if user_value(key='Timer', value=2):
            return 종료()
        if time_expired(timerId='1'):
            return 리셋()


class 리셋(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        set_user_value(triggerId=99990020, key='TimerReset', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='Timer', value=2):
            return 종료()
        if true():
            return 대기()


class 종료(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        set_user_value(triggerId=99990020, key='TimerReset', value=0)


