""" trigger/02020051_bf/105_summon_mob.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[1003], isStart=True)
        start_combine_spawn(groupId=[1002], isStart=False)

    def on_tick(self) -> state.State:
        if user_value(key='Summon_monster', value=1):
            return 몬스터등장()


class 몬스터등장(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[1003], isStart=False)
        start_combine_spawn(groupId=[1002], isStart=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 리셋()


class 리셋(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Summon_monster', value=2):
            return 대기()


