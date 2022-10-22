""" trigger/02000281_bf/move07.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[807], enabled=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[187]):
            return 발판발동()


class 발판발동(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30, clearAtZero=False)
        set_breakable(triggerIds=[807], enabled=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 대기()


