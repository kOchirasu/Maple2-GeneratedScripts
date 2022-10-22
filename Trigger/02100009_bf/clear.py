""" trigger/02100009_bf/clear.xml """
from common import *
import state


class 끝1(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1000049], isEnable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 끝2()


class 끝2(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 끝3()


class 끝3(state.State):
    def on_enter(self):
        add_buff(boxIds=[100000002], skillId=50000217, level=1, arg4=True, arg5=False)
        set_skill(triggerIds=[1000049], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return None


