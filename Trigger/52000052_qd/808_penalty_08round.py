""" trigger/52000052_qd/808_penalty_08round.xml """
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
        create_monster(spawnIds=[90886,90888], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveStart02()


class FirstWaveStart02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90881,90883], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart01()


class SecondWaveStart01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90890,90892], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveStart02()


class SecondWaveStart02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90897,90899], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[90880,90881,90882,90883,90884,90885,90886,90887,90888,90889,90890,90891,90892,90893,90894,90895,90896,90897,90898,90899]):
            return PenaltyFinished01()


class PenaltyFinished01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[90880,90881,90882,90883,90884,90885,90886,90887,90888,90889,90890,90891,90892,90893,90894,90895,90896,90897,90898,90899])
        set_user_value(triggerId=908, key='PenaltyFinish', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PenaltyFinished02()


class PenaltyFinished02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


