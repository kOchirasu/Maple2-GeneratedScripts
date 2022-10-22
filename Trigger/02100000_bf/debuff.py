""" trigger/02100000_bf/debuff.xml """
from common import *
import state


class 유저감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=70000130, level=1, arg4=False, arg5=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버프_2()


class 버프_2(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=70000130, level=1, arg4=False, arg5=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버프_3()


class 버프_3(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=70000130, level=1, arg4=False, arg5=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버프_4()


class 버프_4(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=70000130, level=1, arg4=False, arg5=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버프_5()


class 버프_5(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=70000131, level=1, arg4=False, arg5=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 버프()


