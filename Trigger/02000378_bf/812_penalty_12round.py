""" trigger/02000378_bf/812_penalty_12round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PenaltyMob', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='PenaltyMob', value=1):
            return Ready()


class Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveStart01()


class FirstWaveStart01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91280,91282,91284,91286,91288], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveStart02()


class FirstWaveStart02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91281,91283,91285,91287,91289], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart01()


class SecondWaveStart01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91290,91292,91294,91296,91298], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveStart02()


class SecondWaveStart02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91291,91293,91295,91297,91299], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[91280,91281,91282,91283,91284,91285,91286,91287,91288,91289,91290,91291,91292,91293,91294,91295,91296,91297,91298,91299]):
            return PenaltyFinished01()


class PenaltyFinished01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[91280,91281,91282,91283,91284,91285,91286,91287,91288,91289,91290,91291,91292,91293,91294,91295,91296,91297,91298,91299])
        set_user_value(triggerId=912, key='PenaltyFinish', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PenaltyFinished02()


class PenaltyFinished02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


