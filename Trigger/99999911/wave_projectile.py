""" trigger/99999911/wave_projectile.xml """
from common import *
import state


#  플레이어 감지 
class Round_check(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Round_01', value=1):
            return Round_01()
        if user_value(key='Round_02', value=1):
            return Round_02()
        if user_value(key='Round_03', value=1):
            return None # Missing State: Round_03
        if user_value(key='Round_04', value=1):
            return None # Missing State: Round_04


class Round_01(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return Round_01_Random_01()
        if random_condition(rate=1):
            return Round_01_Random_02()
        if random_condition(rate=1):
            return Round_01_Random_03()
        if random_condition(rate=1):
            return Round_01_Random_04()
        if random_condition(rate=1):
            return Round_01_Random_05()
        if random_condition(rate=1):
            return Round_01_Random_06()


class Round_01_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()


class Round_01_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=True)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()


class Round_01_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[203], arg2=True)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()


class Round_01_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=True)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()


class Round_01_Random_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401], arg2=True)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()


class Round_01_Random_06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[402], arg2=True)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()


class Round_02(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return Round_02_Random_01()
        if random_condition(rate=1):
            return Round_02_Random_02()
        if random_condition(rate=1):
            return Round_02_Random_03()
        if random_condition(rate=1):
            return Round_02_Random_04()
        if random_condition(rate=1):
            return Round_02_Random_05()
        if random_condition(rate=1):
            return Round_02_Random_06()


class Round_02_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True, arg3=0)
        create_monster(spawnIds=[202], arg2=True, arg3=2)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return Round_02()
        if user_value(key='Round_02', value=0):
            return Round_check()


class Round_02_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=True, arg3=0)
        create_monster(spawnIds=[201], arg2=True, arg3=2)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return Round_02()
        if user_value(key='Round_02', value=0):
            return Round_check()


class Round_02_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[203], arg2=True, arg3=0)
        create_monster(spawnIds=[204], arg2=True, arg3=2)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return Round_02()
        if user_value(key='Round_02', value=0):
            return Round_check()


class Round_02_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=True, arg3=0)
        create_monster(spawnIds=[203], arg2=True, arg3=2)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return Round_02()
        if user_value(key='Round_02', value=0):
            return Round_check()


class Round_02_Random_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401], arg2=True, arg3=0)
        create_monster(spawnIds=[401], arg2=True, arg3=2)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return Round_02()
        if user_value(key='Round_02', value=0):
            return Round_check()


class Round_02_Random_06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[402], arg2=True, arg3=0)
        create_monster(spawnIds=[402], arg2=True, arg3=2)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return Round_02()
        if user_value(key='Round_02', value=0):
            return Round_check()


