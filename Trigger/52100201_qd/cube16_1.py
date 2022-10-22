""" trigger/52100201_qd/cube16_1.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='CubeOff', value=1):
            return Off_1()


class Off_1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return On_1()


class On_1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return Off_2()


class Off_2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return On_2()


class On_2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return Off_3()


class Off_3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return On_3()


class On_3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return Off_4()


class Off_4(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=150):
            return On_4()


class On_4(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=150):
            return Off_5()


class Off_5(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=150):
            return On_5()


class On_5(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=150):
            return Off_6()


class Off_6(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=150):
            return On_6()


class On_6(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=150):
            return Off_7()


class Off_7(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5028], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            set_user_value(triggerId=920016, key='CubeOff', value=0)
            set_user_value(triggerId=910016, key='Cube', value=2)
            return 대기()


