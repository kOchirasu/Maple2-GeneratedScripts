""" trigger/80000014_bonus/lever.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001314], state=1)
        set_mesh(triggerIds=[3501,3502,3503,3504,3505,3506], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 반응대기()


class 반응대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 안내()
        if object_interacted(interactIds=[10001314], arg2=0):
            return 문열림()


class 안내(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$80000014_bonus__lever__0$', arg3='2000')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001314], arg2=0):
            return 문열림()
        if wait_tick(waitTick=5000):
            return 반응대기()


class 문열림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3501,3502,3503,3504,3505,3506], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


