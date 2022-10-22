""" trigger/02020300_bf/elevator.xml """
from common import *
import state


class 메시지_대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='elevator', value=1):
            return 엘리베이터_정지()


class 엘리베이터_정지(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020300_BF__MAIN__12$', arg3='5000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            set_breakable(triggerIds=[5001], enabled=False)
            return 종료()


class 종료(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='elevator', value=0):
            return 메시지_대기()


