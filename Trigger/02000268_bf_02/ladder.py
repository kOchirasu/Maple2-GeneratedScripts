""" trigger/02000268_bf_02/ladder.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303,304,305], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000456], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000456], arg2=0):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303,304,305], visible=True, arg3=0, arg4=500, arg5=0)
        set_timer(timerId='10', seconds=10, clearAtZero=False, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            set_mesh(triggerIds=[305,304,303,302,301], visible=False, arg3=0, arg4=500, arg5=0)
            return 재사용대기()


class 재사용대기(state.State):
    def on_enter(self):
        set_timer(timerId='170', seconds=170, clearAtZero=False, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='170'):
            return 대기()


