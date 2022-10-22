""" trigger/52000076_qd/wall_12.xml """
from common import *
import state


class 벽재생(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31201,31202,31203,31204,31205,31206,31207,31208,31209,31210,31211,31212,31213,31214,31215,31216,31217,31218,31219,31220,31221], visible=True, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[112]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31201,31202,31203,31204,31205,31206,31207,31208,31209,31210,31211,31212,31213,31214,31215,31216,31217,31218,31219,31220,31221], visible=False, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[112]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽재생()


