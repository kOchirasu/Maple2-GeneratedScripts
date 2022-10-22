""" trigger/02020061_bf/message.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020061_BF__MESSAGE__0$', arg3='5000')

    def on_tick(self) -> state.State:
        if user_value(key='FieldGameStart', value=1):
            return 종료()
        if user_value(key='FieldGameStart', value=2):
            return 종료()
        if wait_tick(waitTick=5000):
            return 대기()


class 종료(state.State):
    pass


