""" trigger/02000277_bf/mesh_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000633], state=1)
        set_mesh(triggerIds=[10000], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000633], arg2=0):
            return 열기()


class 열기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10000], visible=False)
        set_timer(timerId='1', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


