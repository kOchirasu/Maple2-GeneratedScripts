""" trigger/02000441_bf/boss_1.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='monster_buff', value=1):
            return 몬스터_사망()


class 몬스터_사망(state.State):
    def on_tick(self) -> state.State:
        if any_one():
            return 초강력버프()


class 초강력버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[401,402], skillId=49200001, level=1, arg4=True)

    def on_tick(self) -> state.State:
        if true():
            return None


