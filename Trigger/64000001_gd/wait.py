""" trigger/64000001_gd/wait.xml """
from common import *
import state


class 시간표확인(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10, clearAtZero=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=104, boxId=6):
            return 시작()
        if time_expired(timerId='10'):
            return 시간표확인()


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='88', seconds=1200, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='88'):
            return 시간표확인()


