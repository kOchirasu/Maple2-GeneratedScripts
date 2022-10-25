""" trigger/99999883/testtrigger2.xml """
import common


class State1(common.Trigger):
    def on_enter(self):
        self.debug_string(string='현재 State1')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='test', value=1):
            return State2(self.ctx)


class State2(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='test', value=0)
        self.debug_string(string='현재 State2')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return State1(self.ctx)


initial_state = State1
