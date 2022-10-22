""" trigger/02000245_bf/trigger_01_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000302], state=1)
        set_mesh(triggerIds=[701,702], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000302], arg2=0):
            return 개봉()


class 개봉(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[701,702], visible=False)
        set_timer(timerId='1', seconds=180)


