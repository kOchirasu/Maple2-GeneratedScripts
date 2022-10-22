""" trigger/03000112_bf/mesh.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=True, arg3=0, arg4=50, arg5=3)
        set_interact_object(triggerIds=[10000729], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000729], arg2=0):
            return 부서짐()


class 부서짐(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=False, arg3=0, arg4=50, arg5=3)
        set_timer(timerId='25', seconds=25)

    def on_tick(self) -> state.State:
        if time_expired(timerId='25'):
            return 대기()


