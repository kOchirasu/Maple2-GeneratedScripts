""" trigger/02000498_bf/debuff_02.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        set_timer(timerId='3600', seconds=3600)
        add_buff(boxIds=[103], skillId=70000071, level=2, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3600'):
            return 대기()

