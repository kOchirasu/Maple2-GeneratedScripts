""" trigger/82000012_survival/06_deathfromfall.xml """
from common import *
import state


class Setting(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return WaitSomeoneFall()


class WaitSomeoneFall(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return KillSomeoneFall()


class KillSomeoneFall(state.State):
    def on_enter(self):
        add_buff(boxIds=[9100], skillId=70001061, level=1, arg4=False, arg5=False) # 추락사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return KillSomeoneFall()
        if not user_detected(boxIds=[9100]):
            return WaitSomeoneFall()


