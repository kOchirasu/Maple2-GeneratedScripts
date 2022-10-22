""" trigger/02000163_bf/03_doll_trigger.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[402], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000103], arg2=0):
            return 로봇사라짐()


class 로봇사라짐(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[402], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000103], arg2=1):
            return 대기()


