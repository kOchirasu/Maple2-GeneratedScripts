""" trigger/02000136_ad/01_trigger03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[804], visible=False)
        set_interact_object(triggerIds=[10000068], state=1)
        set_mesh(triggerIds=[15], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000068], arg2=0):
            return 발판등장()


class 발판등장(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[15], visible=True)
        set_effect(triggerIds=[804], visible=True)
        set_timer(timerId='2', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()


