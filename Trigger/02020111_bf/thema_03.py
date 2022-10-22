""" trigger/02020111_bf/thema_03.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1004]):
            return 소환준비()


class 소환준비(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 몬스터등장()


class 몬스터등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[161,162,163,164,165,166])

    def on_tick(self) -> state.State:
        if user_value(key='monster_die', value=1):
            return 몬스터소멸()
        if monster_dead(boxIds=[161,162,163,164,165,166]):
            return 대기()


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='monster_die', value=1):
            return 몬스터소멸()
        if wait_tick(waitTick=10000):
            return 몬스터등장()


class 몬스터소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[161,162,163,164,165,166])

    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakFail', value=1):
            return 시작()


