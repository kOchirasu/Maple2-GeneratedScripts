""" trigger/66200001_gd/08_cheerupskill.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='CheerUpTimer', value=1):
            return CheerUpTimer_20()


class CheerUpTimer_20(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=20, clearAtZero=True, display=False) # 20sec

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return GiveCheerUp()


class GiveCheerUp(state.State):
    def on_enter(self):
        add_buff(boxIds=[9001], skillId=70000086, level=1, arg4=False, arg5=False) # 할 수 있어 버프

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Reset()


#  Reset 
class Reset(state.State):
    def on_enter(self):
        set_user_value(key='CheerUpTimer', value=0)
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


