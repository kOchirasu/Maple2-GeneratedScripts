""" trigger/02020036_bf/100006_timeevent_triggervalue.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='EventStart', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='EventStart', value=1):
            return PuzzleOn()


class PuzzleOn(state.State):
    def on_enter(self):
        set_user_value(key='EventStart', value=0)
        set_user_value(triggerId=16000, key='TimeEventOn', value=1)

    def on_tick(self) -> state.State:
        if wait_seconds_user_value(key='TimeEventLifeTime'):
            return PuzzleOff()


class PuzzleOff(state.State):
    def on_enter(self):
        set_user_value(triggerId=16000, key='TimeEventOn', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


