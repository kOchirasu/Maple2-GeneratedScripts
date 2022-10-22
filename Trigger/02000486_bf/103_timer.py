""" trigger/02000486_bf/103_timer.xml """
from common import *
import state


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if any_one():
            return 타이머()


class 타이머(state.State):
    def on_enter(self):
        set_timer(timerId='999', seconds=240, clearAtZero=True, display=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 설명()


class 설명(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000486_BF__103_TIMER__0$', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=239000):
            return 종료()
        if all_of():
            return 타이머종료()


class 종료(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000486_BF__103_TIMER__1$', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


class 타이머종료(state.State):
    def on_enter(self):
        reset_timer(timerId='999')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


