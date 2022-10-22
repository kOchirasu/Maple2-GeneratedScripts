""" trigger/02020112_bf/reconnect.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Reconnect', value=1):
            return 버프쏴주기()


class 버프쏴주기(state.State):
    def on_enter(self):
        add_buff(boxIds=[916], skillId=70002105, level=1, arg5=False)
        set_timer(timerId='1', seconds=5, clearAtZero=False, display=False)

    def on_tick(self) -> state.State:
        if user_value(key='Reconnect', value=2):
            return 종료()
        if time_expired(timerId='1'):
            return 대기()


class 종료(state.State):
    def on_enter(self):
        add_buff(boxIds=[931], skillId=70002112, level=1, arg5=False)


