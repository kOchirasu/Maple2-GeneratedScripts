""" trigger/02000317_bf/vehicle.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001047], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001047], arg2=0):
            return hide()

    def on_exit(self):
        set_interact_object(triggerIds=[10001047], state=2)


class hide(state.State):
    pass


