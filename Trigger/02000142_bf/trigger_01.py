""" trigger/02000142_bf/trigger_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[7000], enabled=False)
        set_interact_object(triggerIds=[10000245], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000245], arg2=0):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=15, clearAtZero=False)
        set_breakable(triggerIds=[7000], enabled=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()

    def on_exit(self):
        reset_timer(timerId='1')


