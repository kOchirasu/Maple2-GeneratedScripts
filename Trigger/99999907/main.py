""" trigger/99999907/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000019], state=1)
        set_interact_object(triggerIds=[12000020], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000019], arg2=0):
            return 리셋()
        if object_interacted(interactIds=[12000020], arg2=0):
            return 리셋()


class 리셋(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 대기()


