""" trigger/02000252_bf/bigdoor_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[161,162,163,164], visible=True)
        set_interact_object(triggerIds=[10000403], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000403], arg2=0):
            return 열기()


class 열기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[161,162,163,164], visible=False)


