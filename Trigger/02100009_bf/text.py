""" trigger/02100009_bf/text.xml """
from common import *
import state


class 유저감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 알림()


class 알림(state.State):
    def on_tick(self) -> state.State:
        if any_one():
            return 알림_2()
        if all_of():
            return 완료알림()

    def on_exit(self):
        reset_timer(timerId='10000')


class 알림_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 알림_3()

    def on_exit(self):
        set_event_ui(type=1, arg2='$02100009_BF__resurrection_2__0$', arg3='4000')


class 알림_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 알림()
        if all_of():
            return 완료알림()


class 완료알림(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return None


