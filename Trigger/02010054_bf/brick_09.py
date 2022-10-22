""" trigger/02010054_bf/brick_09.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[34009], visible=True, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[7009], isEnable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1109]):
            return 발판()


class 발판(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7009], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            set_mesh(triggerIds=[34009], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass

