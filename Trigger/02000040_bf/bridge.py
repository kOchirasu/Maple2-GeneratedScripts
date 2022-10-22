""" trigger/02000040_bf/bridge.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000319], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000319], arg2=0):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303], visible=True, arg3=0, arg4=500, arg5=2)
        set_timer(timerId='3', seconds=3, clearAtZero=False, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[303,302,301], visible=False, arg3=0, arg4=500, arg5=2)
            return 재사용대기()


class 재사용대기(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10, clearAtZero=False, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 대기()


