""" trigger/02000207_bf/arm01.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ZakumArmDeath01', value=1):
            return 트로피지급()


class 트로피지급(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='ZakumArmDeath01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


