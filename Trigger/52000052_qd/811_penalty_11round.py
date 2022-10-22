""" trigger/52000052_qd/811_penalty_11round.xml """
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
        create_monster(spawnIds=[91182,91188], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveStart02()


class FirstWaveStart02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91183,91187], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart01()


class SecondWaveStart01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91194,91198], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveStart02()


class SecondWaveStart02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91191,91195], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[91180,91181,91182,91183,91184,91185,91186,91187,91188,91189,91190,91191,91192,91193,91194,91195,91196,91197,91198,91199]):
            return PenaltyFinished01()


class PenaltyFinished01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[91180,91181,91182,91183,91184,91185,91186,91187,91188,91189,91190,91191,91192,91193,91194,91195,91196,91197,91198,91199])
        set_user_value(triggerId=911, key='PenaltyFinish', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PenaltyFinished02()


class PenaltyFinished02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


