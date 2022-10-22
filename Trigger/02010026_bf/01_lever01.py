""" trigger/02010026_bf/01_lever01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1000,1001,1002,1003,1004], visible=False, arg3=0, arg4=0, arg5=5)
        set_interact_object(triggerIds=[10000908], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000908], arg2=0):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[1000,1001,1002,1003,1004], visible=True, meshCount=5, arg4=100, delay=100)
        set_timer(timerId='2', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 재사용대기()


class 재사용대기(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 대기()


