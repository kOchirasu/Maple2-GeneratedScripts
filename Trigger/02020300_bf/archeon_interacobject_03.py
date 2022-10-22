""" trigger/02020300_bf/archeon_interacobject_03.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002188], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002188], arg2=0):
            set_interact_object(triggerIds=[10002188], state=2)
            return 재활성대기()


class 재활성대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=60000):
            return 시작()


class 종료(state.State):
    pass


