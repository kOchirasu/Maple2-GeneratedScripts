""" trigger/02000328_bf/buff.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[999998]):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[999998], skillId=70000111, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 대기()


