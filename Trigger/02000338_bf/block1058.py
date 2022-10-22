""" trigger/02000338_bf/block1058.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1058], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10058]):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 진행1()


class 진행1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1058], visible=False, arg3=0, arg4=0, arg5=2)


