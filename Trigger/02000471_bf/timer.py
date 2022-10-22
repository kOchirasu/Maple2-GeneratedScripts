""" trigger/02000471_bf/timer.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_user_value(triggerId=2040301, key='TimerEnd', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TimerStart', value=1):
            return start()


class start(state.State):
    def on_enter(self):
        set_timer(timerId='Timer', seconds=420, clearAtZero=True, display=True, arg5=0)
        set_event_ui(type=1, arg2='$02000471_BF__TIMER__0$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='Timer'):
            return end_fail()
        if user_value(key='InteractClear', value=1):
            return end_clear()


class end_fail(state.State):
    def on_enter(self):
        set_user_value(triggerId=2040301, key='TimerEnd', value=1)
        reset_timer(timerId='Timer')


class end_clear(state.State):
    def on_enter(self):
        set_user_value(triggerId=2040301, key='InteractClear', value=1)
        reset_timer(timerId='Timer')


