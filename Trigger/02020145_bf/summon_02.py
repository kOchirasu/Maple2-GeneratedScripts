""" trigger/02020145_bf/summon_02.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 소환준비()


class 소환준비(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Summon_Enemy_1', value=0):
            return 시작()
        if user_value(key='Summon_Enemy_1', value=1):
            return 몬스터등장()


class 몬스터등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[121,122,123,124,131,132,133,134])

    def on_tick(self) -> state.State:
        if user_value(key='Summon_Enemy_1', value=0):
            return 시작()
        if user_value(key='Summon_Enemy_2', value=1):
            return 몬스터등장_2()


class 몬스터등장_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[121,122,123,124,131,132,133,134])

    def on_tick(self) -> state.State:
        if user_value(key='Summon_Enemy_1', value=0):
            return 시작()


