""" trigger/02020101_bf/timer.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=900002, key='TimerReset', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TimerStart', value=1):
            return 타이머1_시작()


class 타이머1_시작(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=20, clearAtZero=True, display=True, arg5=-40)

    def on_tick(self) -> state.State:
        if user_value(key='TimerStart', value=9):
            return 종료()
        if user_value(key='TimerStart', value=0):
            return 리셋_1()
        if time_expired(timerId='1'):
            return 리셋_1()


class 리셋_1(state.State):
    def on_enter(self):
        set_user_value(triggerId=900002, key='TimerReset', value=1)
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if user_value(key='TimerStart', value=9):
            return 종료()
        if user_value(key='TimerStart', value=2):
            return 타이머2_시작()


class 타이머2_시작(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=20, clearAtZero=True, display=True, arg5=-40)

    def on_tick(self) -> state.State:
        if user_value(key='TimerStart', value=9):
            return 종료()
        if user_value(key='TimerStart', value=0):
            return 리셋_2()
        if time_expired(timerId='2'):
            return 리셋_2()


class 리셋_2(state.State):
    def on_enter(self):
        set_user_value(triggerId=900002, key='TimerReset', value=2)
        reset_timer(timerId='2')

    def on_tick(self) -> state.State:
        if user_value(key='TimerStart', value=9):
            return 종료()
        if user_value(key='TimerStart', value=3):
            return 타이머3_시작()


class 타이머3_시작(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=20, clearAtZero=True, display=True, arg5=-40)

    def on_tick(self) -> state.State:
        if user_value(key='TimerStart', value=9):
            return 종료()
        if user_value(key='TimerStart', value=0):
            return 리셋_3()
        if time_expired(timerId='3'):
            return 리셋_3()


class 리셋_3(state.State):
    def on_enter(self):
        set_user_value(triggerId=900002, key='TimerReset', value=3)
        reset_timer(timerId='3')

    def on_tick(self) -> state.State:
        if user_value(key='TimerStart', value=9):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        reset_timer(timerId='2')
        reset_timer(timerId='3')


