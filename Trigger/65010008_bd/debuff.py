""" trigger/65010008_bd/debuff.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 디버프()


class 디버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=70000040, level=1, arg4=False, arg5=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대기()


