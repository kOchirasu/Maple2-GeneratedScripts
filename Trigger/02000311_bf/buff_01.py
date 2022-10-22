""" trigger/02000311_bf/buff_01.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Buff_01', value=1):
            return Buff_Ready()


class Buff_Ready(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return Buff_01()


class Buff_01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return Buff_01_Start()


class Buff_01_Start(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=50003006, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Buff_01()


