""" trigger/02020015_bf/02020015_timer.xml """
from common import *
import state


class 신호대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Timer', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=20, clearAtZero=True, display=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019], visible=False)
        reset_timer(timerId='1')


