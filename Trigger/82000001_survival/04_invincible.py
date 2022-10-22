""" trigger/82000001_survival/04_invincible.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return MakeInvincible()


class MakeInvincible(state.State):
    def on_enter(self):
        add_buff(boxIds=[9000], skillId=71000049, level=1, arg4=False, arg5=False) # 대기공간 무적

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return MakeInvincible()
        if user_value(key='InvincibleOff', value=1):
            return Quit()


class Quit(state.State):
    pass


