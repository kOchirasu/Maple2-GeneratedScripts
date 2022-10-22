""" trigger/03000049_bf/trigger_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000289], state=1)
        set_effect(triggerIds=[101], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000289], arg2=0):
            return 비내림()


class 비내림(state.State):
    def on_enter(self):
        set_effect(triggerIds=[101], visible=True)
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


