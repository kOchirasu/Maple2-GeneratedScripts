""" trigger/02000284_bf/ladder02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000436], state=1)
        set_mesh(triggerIds=[321,322,323,324], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000436], arg2=0):
            return 사다리생성()


class 사다리생성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000436], state=0)
        set_mesh(triggerIds=[321,322,323,324], visible=True, arg3=0, arg4=500, arg5=0)
        set_timer(timerId='1500', seconds=1500, clearAtZero=False, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1500'):
            return 대기()


