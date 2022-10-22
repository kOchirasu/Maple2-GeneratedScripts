""" trigger/65010006_bd/debuff.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 체크()


class 체크(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 디버프()


class 디버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[102], skillId=70000040, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 체크()


