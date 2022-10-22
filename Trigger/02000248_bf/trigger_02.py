""" trigger/02000248_bf/trigger_02.xml """
from common import *
import state


class ready(state.State):
    def on_enter(self):
        set_cube(triggerIds=[2101,2102,2103,2104,2105], isVisible=True)


class objectset(state.State):
    def on_enter(self):
        set_cube(triggerIds=[2101,2102,2103,2104,2105], randomCount=1, isVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return WaitTick()


class WaitTick(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return objectset()


