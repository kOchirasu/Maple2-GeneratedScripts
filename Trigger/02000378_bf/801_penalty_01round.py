""" trigger/02000378_bf/801_penalty_01round.xml """
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
        create_monster(spawnIds=[90180,90182,90184,90186,90188], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveStart02()


class FirstWaveStart02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90181,90183,90185,90187,90189], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart01()


class SecondWaveStart01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90190,90192,90194,90196,90198], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveStart02()


class SecondWaveStart02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90191,90193,90195,90197,90199], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[90180,90181,90182,90183,90184,90185,90186,90187,90188,90189,90190,90191,90192,90193,90194,90195,90196,90197,90198,90199]):
            return PenaltyFinished01()


class PenaltyFinished01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[90180,90181,90182,90183,90184,90185,90186,90187,90188,90189,90190,90191,90192,90193,90194,90195,90196,90197,90198,90199])
        set_user_value(triggerId=901, key='PenaltyFinish', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PenaltyFinished02()


class PenaltyFinished02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


