""" trigger/02010028_bf/mesh01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1000,1001,1002,1003,1004,1005], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000902], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000902], arg2=0):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1000,1001,1002,1003,1004,1005], visible=False, arg3=0, arg4=0, arg5=7)
        set_timer(timerId='2', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 재사용대기()


class 재사용대기(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 대기()


