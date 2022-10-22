""" trigger/02020019_bf/02020019_specialtimer.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SpecialTimer', value=1):
            return 타이머시작()


class 타이머시작(state.State):
    def on_enter(self):
        set_timer(timerId='SpecialTimer', seconds=180, clearAtZero=True, display=False)

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크()


class 타이머체크(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='SpecialTimer'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990002, key='SpecialTimer', value=0)
        reset_timer(timerId='SpecialTimer')


