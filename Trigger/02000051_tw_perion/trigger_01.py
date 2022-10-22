""" trigger/02000051_tw_perion/trigger_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000382], state=1)
        set_mesh(triggerIds=[101], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000382], arg2=0):
            return 열림()


class 열림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[101], visible=True)
        set_timer(timerId='1', seconds=15, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


