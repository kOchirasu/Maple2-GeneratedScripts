""" trigger/02010054_bf/buff.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[199], skillId=70000108, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 대기()


