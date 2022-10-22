""" trigger/51000003_dg/wave_projectile_05.xml """
from common import *
import state


#  플레이어 감지 
class Round_check(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[421,422,423,424,425,426,427,428,429,430])

    def on_tick(self) -> state.State:
        if user_value(key='Round_01', value=1):
            return Round_01_Ready()


class Round_01_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return Round_01()


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


class Round_01_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[296], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_01()
        if user_value(key='Round_02', value=1):
            return Round_02()
        if user_value(key='Reset', value=1):
            return End()


class Round_01_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[297], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_01()
        if user_value(key='Round_02', value=1):
            return Round_02()
        if user_value(key='Reset', value=1):
            return End()


class Round_01_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[298], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_01()
        if user_value(key='Round_02', value=1):
            return Round_02()
        if user_value(key='Reset', value=1):
            return End()


class Round_01_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[299], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_01()
        if user_value(key='Round_02', value=1):
            return Round_02()
        if user_value(key='Reset', value=1):
            return End()


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


class Round_02_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[414], arg2=True, arg3=0)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_02()
        if user_value(key='Round_03', value=1):
            return None # Missing State: Round_03
        if user_value(key='Reset', value=1):
            return End()
        if user_value(key='Reset', value=1):
            return End()


class Round_02_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[415], arg2=True, arg3=0)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_02()
        if user_value(key='Round_03', value=1):
            return None # Missing State: Round_03
        if user_value(key='Reset', value=1):
            return End()
        if user_value(key='Reset', value=1):
            return End()


class Round_02_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[416], arg2=True, arg3=0)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_02()
        if user_value(key='Round_03', value=1):
            return None # Missing State: Round_03
        if user_value(key='Reset', value=1):
            return End()
        if user_value(key='Reset', value=1):
            return End()


class Round_02_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[417], arg2=True, arg3=0)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_02()
        if user_value(key='Round_03', value=1):
            return None # Missing State: Round_03
        if user_value(key='Reset', value=1):
            return End()
        if user_value(key='Reset', value=1):
            return End()


class End(state.State):
    pass


