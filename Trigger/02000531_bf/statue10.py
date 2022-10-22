""" trigger/02000531_bf/statue10.xml """
from common import *
import state


class 세팅(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 수신대기()


class 수신대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='StatueHuman01Death', value=1):
            set_mesh(triggerIds=[10], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10], visible=False, arg3=0, arg4=0, arg5=0)

