""" trigger/52010056_qd/buff.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Ready()


class Ready(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[3]):
            return Buff_B()
        if quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[2]):
            return Buff_B()
        if quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[1]):
            return Buff_B()
        if quest_user_detected(boxIds=[2001], questIds=[91000053], questStates=[3]):
            return Buff_A()
        if quest_user_detected(boxIds=[2001], questIds=[91000053], questStates=[2]):
            return Buff_A()
        if quest_user_detected(boxIds=[2001], questIds=[91000053], questStates=[1]):
            return Buff_A()
        if quest_user_detected(boxIds=[2001], questIds=[91000052], questStates=[3]):
            return Buff_A()


class Buff_A(state.State):
    def on_enter(self):
        add_buff(boxIds=[2001], skillId=99910300, level=1, arg4=False, arg5=True) # 트리스탄 변신
        add_buff(boxIds=[2001], skillId=99910300, level=1, arg4=False, arg5=False) # 트리스탄 변신

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Ready()


class Buff_B(state.State):
    def on_enter(self):
        add_buff(boxIds=[2001], skillId=99910330, level=1, arg4=False, arg5=True) # 트리스탄 변신
        add_buff(boxIds=[2001], skillId=99910330, level=1, arg4=False, arg5=False) # 트리스탄 변신

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Ready()


