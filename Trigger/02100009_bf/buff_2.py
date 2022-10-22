""" trigger/02100009_bf/buff_2.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=50000206, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 대기()


