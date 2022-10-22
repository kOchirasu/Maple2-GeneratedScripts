""" trigger/02000011_bf/move.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2, clearAtZero=False)
        set_breakable(triggerIds=[7000], enabled=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 반응대기()


class 반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000361], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000361], arg2=0):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=6, clearAtZero=False)
        set_breakable(triggerIds=[7000], enabled=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 대기()


