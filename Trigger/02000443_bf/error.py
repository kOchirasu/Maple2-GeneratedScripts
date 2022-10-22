""" trigger/02000443_bf/error.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return buff_1()


class buff_1(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=49200002, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=60000):
            return buff_2()
        if user_value(key='debuff', value=1):
            return None # Missing State: 끝


class buff_2(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=49200002, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=60000):
            return buff_1()


