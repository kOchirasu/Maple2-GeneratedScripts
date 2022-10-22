""" trigger/02000375_bf/1122000.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_sound(triggerId=13500, arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='ChangeBGM', value=1):
            return BGM변경()


class BGM변경(state.State):
    def on_enter(self):
        set_sound(triggerId=13500, arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 종료()


class 종료(state.State):
    pass


