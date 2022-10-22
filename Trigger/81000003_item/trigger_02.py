""" trigger/81000003_item/trigger_02.xml """
from common import *
import state


class 레버(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000225], state=1)
        set_mesh(triggerIds=[530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000225], arg2=0):
            return 바닥열기()


class 바닥열기(state.State):
    def on_enter(self):
        set_timer(timerId='8', seconds=200)
        set_mesh(triggerIds=[530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='8'):
            return 레버()


