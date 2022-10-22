""" trigger/02020019_bf/02020019_timer.xml """
from common import *
import state


#  <라운드 시작하면서 5분 시간 제한 타이머> 
class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Timer', value=1):
            return 타이머시작()


class 타이머시작(state.State):
    def on_enter(self):
        set_timer(timerId='BattleTimer', seconds=300, clearAtZero=True, display=True)

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크()


class 타이머체크(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='BattleTimer'):
            return 종료()
        if user_value(key='TimerReset', value=1):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        reset_timer(timerId='BattleTimer')
        set_user_value(triggerId=99990002, key='Timer', value=2)


