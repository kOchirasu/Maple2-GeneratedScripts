""" trigger/99999883/testtrigger2.xml """
from common import *
import state


class State1(state.State):
    def on_enter(self):
        debug_string(string='현재 State1')

    def on_tick(self) -> state.State:
        if user_value(key='test', value=1):
            return State2()


class State2(state.State):
    def on_enter(self):
        set_user_value(key='test', value=0)
        debug_string(string='현재 State2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return State1()


