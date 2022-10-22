""" trigger/02000311_bf/buff_02.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Buff_02', value=1):
            return Buff_02_Ready()


class Buff_02_Ready(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return Buff_02()


class Buff_02(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return Buff_02_Start()


class Buff_02_Start(state.State):
    def on_enter(self):
        add_buff(boxIds=[702], skillId=50003006, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Buff_02()


