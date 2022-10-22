""" trigger/03000050_tw/mesh.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=200, arg5=2)
        set_interact_object(triggerIds=[10000730], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000730], arg2=0):
            return 부서짐()


class 부서짐(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=200, arg5=2)
        set_timer(timerId='25', seconds=25)

    def on_tick(self) -> state.State:
        if time_expired(timerId='25'):
            return 대기()

