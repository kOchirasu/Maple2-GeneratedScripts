""" trigger/02020051_bf/106_summon_mob_2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[1001], isStart=False)

    def on_tick(self) -> state.State:
        if user_value(key='Summon_monster_2', value=1):
            return 몬스터등장()


class 몬스터등장(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[1001], isStart=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 리셋()


class 리셋(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Summon_monster_2', value=2):
            return 대기()


