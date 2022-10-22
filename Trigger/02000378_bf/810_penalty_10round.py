""" trigger/02000378_bf/810_penalty_10round.xml """
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
        create_monster(spawnIds=[91080,91082,91084,91086,91088], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveStart02()


class FirstWaveStart02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91081,91083,91085,91087,91089], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart01()


class SecondWaveStart01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91090,91092,91094,91096,91098], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveStart02()


class SecondWaveStart02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91091,91093,91095,91097,91099], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[91080,91081,91082,91083,91084,91085,91086,91087,91088,91089,91090,91091,91092,91093,91094,91095,91096,91097,91098,91099]):
            return PenaltyFinished01()


class PenaltyFinished01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[91080,91081,91082,91083,91084,91085,91086,91087,91088,91089,91090,91091,91092,91093,91094,91095,91096,91097,91098,91099])
        set_user_value(triggerId=910, key='PenaltyFinish', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PenaltyFinished02()


class PenaltyFinished02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


