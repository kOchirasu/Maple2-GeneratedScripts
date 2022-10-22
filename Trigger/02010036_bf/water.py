""" trigger/02010036_bf/water.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=30, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 부서짐()


class 부서짐(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=30, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[101]):
            return 대기()


