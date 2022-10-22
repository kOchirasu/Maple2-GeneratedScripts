""" trigger/02000486_bf/106_resurrection_2.xml """
from common import *
import state


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[901]):
            return 타임()


class 타임(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=240000):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        set_ai_extra_data(key='RageBuff_3', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 버프_종료()


class 버프_종료(state.State):
    def on_enter(self):
        set_ai_extra_data(key='RageBuff_3', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


