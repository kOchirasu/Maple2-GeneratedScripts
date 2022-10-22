""" trigger/02000312_bf/filter_10.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='1stTreeRemove', value=0)
        set_user_value(key='2ndTreeRemove', value=0)
        set_user_value(key='3rdTreeRemove', value=0)
        set_user_value(key='4thTreeRemove', value=0)
        set_user_value(key='5thTreeRemove', value=0)
        set_user_value(key='6thTreeRemove', value=0)
        set_user_value(key='7thTreeRemove', value=0)
        set_user_value(key='8thTreeRemove', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return CheckStart()


#  제거된 씨앗 체크 
class CheckStart(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Check01()


class Check01(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='1stTreeRemove', value=1):
            return Check02()
        if wait_tick(waitTick=2000):
            return CheckStart()


class Check02(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='2ndTreeRemove', value=1):
            return Check03()
        if wait_tick(waitTick=2000):
            return CheckStart()


class Check03(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='3rdTreeRemove', value=1):
            return Check04()
        if wait_tick(waitTick=2000):
            return CheckStart()


class Check04(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='4thTreeRemove', value=1):
            return Check05()
        if wait_tick(waitTick=2000):
            return CheckStart()


class Check05(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='5thTreeRemove', value=1):
            return Check06()
        if wait_tick(waitTick=2000):
            return CheckStart()


class Check06(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='6thTreeRemove', value=1):
            return Check07()
        if wait_tick(waitTick=2000):
            return CheckStart()


class Check07(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='7thTreeRemove', value=1):
            return Check08()
        if wait_tick(waitTick=2000):
            return CheckStart()


class Check08(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='8thTreeRemove', value=1):
            return BoardApp()
        if wait_tick(waitTick=2000):
            return CheckStart()


class BoardApp(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='BoardApp', value=1)
        set_user_value(triggerId=11, key='MobWaveStop', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


