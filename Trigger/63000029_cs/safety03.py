""" trigger/63000029_cs/safety03.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='SafetyStart', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='SafetyStart', value=1):
            return Enter01()


class Enter01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return PCTeleport01()


class PCTeleport01(state.State):
    def on_enter(self):
        move_user(mapId=63000029, portalId=12, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Reset01()


class Reset01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return Enter01()


