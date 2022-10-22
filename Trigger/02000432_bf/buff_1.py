""" trigger/02000432_bf/buff_1.xml """
from common import *
import state


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2001]):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[2001], skillId=40501001, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 사망()


class 사망(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 사망_버프제거()


class 사망_버프제거(state.State):
    def on_enter(self):
        add_buff(boxIds=[2002], skillId=40501005, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


