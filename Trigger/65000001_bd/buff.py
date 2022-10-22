""" trigger/65000001_bd/buff.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        add_buff(boxIds=[102], skillId=70000040, level=1, arg4=False, arg5=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


