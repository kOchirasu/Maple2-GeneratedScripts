""" trigger/02020111_bf/message.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Message', value=0):
            return 메세지출력()


class 메세지출력(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020111_BF__MESSAGE__0$', arg3='4000')

    def on_tick(self) -> state.State:
        if user_value(key='Message', value=1):
            return 시작()


