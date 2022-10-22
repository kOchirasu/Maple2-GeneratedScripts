""" trigger/02000281_bf/move02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[802], enabled=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[182]):
            return 발판발동()


class 발판발동(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30, clearAtZero=False)
        set_breakable(triggerIds=[802], enabled=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 대기()


