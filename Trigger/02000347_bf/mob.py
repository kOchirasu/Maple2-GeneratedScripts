""" trigger/02000347_bf/mob.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[60002]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000804], arg2=0):
            return 랜덤몬스터소환()
        if monster_dead(boxIds=[101]):
            return 종료()


class 랜덤몬스터소환(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return 번소환1()
        if random_condition(rate=10):
            return 번소환2()
        if random_condition(rate=10):
            return 번소환3()
        if random_condition(rate=10):
            return 번소환4()
        if random_condition(rate=10):
            return 번소환5()
        if random_condition(rate=10):
            return 번소환6()
        if random_condition(rate=10):
            return 번소환7()
        if random_condition(rate=10):
            return 번소환8()
        if random_condition(rate=10):
            return 번소환9()
        if random_condition(rate=10):
            return 번소환10()
        if object_interacted(interactIds=[10000804], arg2=1):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번소환1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001])
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤몬스터소환()
        if object_interacted(interactIds=[10000804], arg2=1):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번소환2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002])
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤몬스터소환()
        if object_interacted(interactIds=[10000804], arg2=1):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번소환3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1003])
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤몬스터소환()
        if object_interacted(interactIds=[10000804], arg2=1):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번소환4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1004])
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤몬스터소환()
        if object_interacted(interactIds=[10000804], arg2=1):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번소환5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1005])
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤몬스터소환()
        if object_interacted(interactIds=[10000804], arg2=1):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번소환6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1006])
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤몬스터소환()
        if object_interacted(interactIds=[10000804], arg2=1):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번소환7(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1007])
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤몬스터소환()
        if object_interacted(interactIds=[10000804], arg2=1):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번소환8(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1008])
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤몬스터소환()
        if object_interacted(interactIds=[10000804], arg2=1):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번소환9(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1009])
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤몬스터소환()
        if object_interacted(interactIds=[10000804], arg2=1):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번소환10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1010])
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤몬스터소환()
        if object_interacted(interactIds=[10000804], arg2=1):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])


