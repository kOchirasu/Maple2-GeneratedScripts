""" trigger/02000347_bf/guide.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[60002]):
            return 대기_02()


class 대기_02(state.State):
    def on_enter(self):
        set_timer(timerId='8', seconds=8)

    def on_tick(self) -> state.State:
        if time_expired(timerId='8'):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000347_BF__MAIN1__5$', arg3='5000', arg4='0')


