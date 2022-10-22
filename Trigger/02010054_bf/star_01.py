""" trigger/02010054_bf/star_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3301,3302,3303,3304,3305], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000856], arg2=0):
            return 소멸()


class 소멸(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3301,3302,3303,3304,3305], visible=True, arg3=0, arg4=500, arg5=3)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3301,3302,3303,3304,3305], visible=False, arg3=0, arg4=900, arg5=2)
            return 종료()


class 종료(state.State):
    pass


