""" trigger/02000486_bf/104_clear.xml """
from common import *
import state


class 끝1(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9901]):
            return 끝2()


class 끝2(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 끝3()


class 끝3(state.State):
    def on_enter(self):
        add_buff(boxIds=[900], skillId=50002505, level=1, arg4=True, arg5=False)
        add_buff(boxIds=[901], skillId=50002505, level=1, arg4=True, arg5=False)
        set_skill(triggerIds=[1000049], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return None


