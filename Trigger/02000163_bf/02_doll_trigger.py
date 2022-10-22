""" trigger/02000163_bf/02_doll_trigger.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000102], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[401], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000102], arg2=0):
            return 로봇사라짐()


class 로봇사라짐(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[401], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000102], arg2=1):
            return 대기()


