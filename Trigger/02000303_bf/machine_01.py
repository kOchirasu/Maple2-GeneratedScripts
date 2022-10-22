""" trigger/02000303_bf/machine_01.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000575], arg2=0):
            set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=2)
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1800000'):
            return None # Missing State: 종료2


