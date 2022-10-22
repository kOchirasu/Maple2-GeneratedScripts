""" trigger/02000431_bf/buff_1.xml """
from common import *
import state


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2199]):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[2199], skillId=40501006, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


