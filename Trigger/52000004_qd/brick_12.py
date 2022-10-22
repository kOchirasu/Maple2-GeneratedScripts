""" trigger/52000004_qd/brick_12.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3112], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[122]):
            return 발판01()


class 발판01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            set_mesh(triggerIds=[3112], visible=False, arg3=0, arg4=0, arg5=0)
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 대기()


