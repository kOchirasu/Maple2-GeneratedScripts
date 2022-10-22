""" trigger/02000486_bf/101_buff.xml """
from common import *
import state


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[900]):
            return 타임()


class 타임(state.State):
    def on_tick(self) -> state.State:
        if any_one():
            return None # Missing State: Move01


class 버프_종료(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


