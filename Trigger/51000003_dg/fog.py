""" trigger/51000003_dg/fog.xml """
from common import *
import state


#  포그 이펙트 
class Round_check(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=False)
        set_effect(triggerIds=[7002], visible=False)
        set_effect(triggerIds=[7003], visible=False)
        set_effect(triggerIds=[7004], visible=False)
        set_effect(triggerIds=[7005], visible=False)
        set_effect(triggerIds=[7010], visible=True)

    def on_tick(self) -> state.State:
        if user_value(key='Round_01', value=1):
            return None # Missing State: Round_01
        if user_value(key='Round_02', value=1):
            return Round_02_Ready()
        if user_value(key='Round_03', value=1):
            return Round_03_Ready()
        if user_value(key='Round_04', value=1):
            return Round_04_Ready()


class Round_02_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return Round_02_Start()


class Round_03_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return Round_03_Start()


class Round_04_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return Round_04_Start()


class Round_05_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return Round_05_Start()


class Round_06_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return Round_06_Start()


class Round_02_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=True)

    def on_tick(self) -> state.State:
        if user_value(key='Round_02', value=0):
            return Round_check()
        if wait_tick(waitTick=30000):
            return Round_check()


class Round_03_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7002], visible=True)

    def on_tick(self) -> state.State:
        if user_value(key='Round_03', value=0):
            return Round_check()
        if wait_tick(waitTick=30000):
            return Round_check()


class Round_04_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7002], visible=True)

    def on_tick(self) -> state.State:
        if user_value(key='Round_04', value=0):
            return Round_check()
        if wait_tick(waitTick=30000):
            return Round_check()


class Round_05_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7003], visible=True)

    def on_tick(self) -> state.State:
        if user_value(key='Round_05', value=0):
            return Round_check()
        if wait_tick(waitTick=30000):
            return Round_check()


class Round_06_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7005], visible=True)

    def on_tick(self) -> state.State:
        if user_value(key='Round_06', value=0):
            return Round_check()
        if wait_tick(waitTick=30000):
            return Round_check()


