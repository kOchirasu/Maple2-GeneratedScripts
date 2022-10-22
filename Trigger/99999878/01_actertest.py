""" trigger/99999878/01_actertest.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_actor(triggerId=1000, visible=True, initialSequence='Closed')
        set_breakable(triggerIds=[2000], enabled=False)
        set_visible_breakable_object(triggerIds=[2000], arg2=True)

    def on_tick(self) -> state.State:
        if check_user():
            return OpenDelay()


class OpenDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Open()


class Open(state.State):
    def on_enter(self):
        set_actor(triggerId=1000, visible=True, initialSequence='Opened')
        set_breakable(triggerIds=[2000], enabled=True)
        set_visible_breakable_object(triggerIds=[2000], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return OffDelay()


class OffDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Off()


class Off(state.State):
    def on_enter(self):
        set_actor(triggerId=1000, visible=False, initialSequence='Opened')
        set_breakable(triggerIds=[2000], enabled=False)
        set_visible_breakable_object(triggerIds=[2000], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait()


