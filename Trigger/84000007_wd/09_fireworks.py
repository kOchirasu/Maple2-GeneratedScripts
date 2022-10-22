""" trigger/84000007_wd/09_fireworks.xml """
from common import *
import state


class Staging(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Fireworks', value=1):
            return Volley_Ready()
        if user_value(key='Fireworks', value=2):
            return Volley_Ready2()


class Volley_Ready(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$84000007_WD__09_FIREWORKS__0$', arg3='3000', arg4='0') # action name="카메라경로를선택한다" arg1="902,903" arg2="1"/

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Volley_Fire()


class Volley_Ready2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$84000007_WD__09_FIREWORKS__1$', arg3='3000', arg4='0') # action name="카메라경로를선택한다" arg1="902,903" arg2="1"/

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Volley_Fire()


class Volley_Fire(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=14000):
            return None


