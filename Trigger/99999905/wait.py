""" trigger/99999905/wait.xml """
from common import *
import state


class 시간표확인(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10, clearAtZero=False)
        set_event_ui(type=1, arg2='$99999905__WAIT__0$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if count_users(boxId=101, boxId=10):
            return 시작()
        if time_expired(timerId='10'):
            return 시간표확인()


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='88', seconds=1200, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='88'):
            return 시간표확인()


