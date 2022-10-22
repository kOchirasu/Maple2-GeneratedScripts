""" trigger/02020111_bf/thema_02.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1003]):
            return 소환준비()


class 소환준비(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 몬스터등장()


class 몬스터등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[151,152,153,154,155,156])

    def on_tick(self) -> state.State:
        if user_value(key='monster_die', value=1):
            return 몬스터소멸()
        if monster_dead(boxIds=[151,152,153,154,155,156]):
            return 대기()


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='monster_die', value=1):
            return 몬스터소멸()
        if wait_tick(waitTick=10000):
            return 몬스터등장()


class 몬스터소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[151,152,153,154,155,156])

    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakFail', value=1):
            return 시작()


