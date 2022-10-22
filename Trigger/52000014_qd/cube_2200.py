""" trigger/52000014_qd/cube_2200.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2200], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2203], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[12200], visible=False) # Fire Cast Sound

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[92200]):
            return 무너짐01()


class 무너짐01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)
        set_effect(triggerIds=[12200], visible=True) # Fire Cast Sound
        set_mesh(triggerIds=[2200], visible=False, arg3=0, arg4=0, arg5=1)
        set_mesh(triggerIds=[2203], visible=False, arg3=1000, arg4=0, arg5=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[12200], visible=False) # Fire Cast Sound


