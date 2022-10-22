""" trigger/51000003_dg/wave_projectile_03.xml """
from common import *
import state


#  플레이어 감지 
class Round_check(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[421,422,423,424,425,426,427,428,429,430])

    def on_tick(self) -> state.State:
        if user_value(key='Round_01', value=1):
            return Round_01_Ready()
        if user_value(key='Round_02', value=1):
            return None # Missing State: Round_02
        if user_value(key='Round_03', value=1):
            return Round_03_Ready()
        if user_value(key='Round_04', value=1):
            return Round_04_Ready()
        if user_value(key='Round_05', value=1):
            return Round_05_Ready()
        if user_value(key='Round_06', value=1):
            return Round_06()


class Round_01_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return Round_01()


class Round_02_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return None # Missing State: Round_02


class Round_03_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return Round_03()


class Round_04_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return Round_04()


class Round_05_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return Round_05()


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


class Round_01_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[211], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_01_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[212], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_01_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[213], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_01_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[214], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_01_Random_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[215], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_03(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return Round_03_Random_01()
        if random_condition(rate=1):
            return Round_03_Random_02()
        if random_condition(rate=1):
            return Round_03_Random_03()
        if random_condition(rate=1):
            return Round_03_Random_04()


class Round_03_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[408], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_03()
        if user_value(key='Round_03', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_03_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[406], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_03()
        if user_value(key='Round_03', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_03_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[403], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_03()
        if user_value(key='Round_03', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_03_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[405], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_03()
        if user_value(key='Round_03', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_04(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return Round_04_Random_01()
        if random_condition(rate=1):
            return Round_04_Random_02()
        if random_condition(rate=1):
            return Round_04_Random_03()
        if random_condition(rate=1):
            return Round_04_Random_04()


class Round_04_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[408], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_04()
        if user_value(key='Round_04', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_04_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[406], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_04()
        if user_value(key='Round_04', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_04_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[403], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_04()
        if user_value(key='Round_04', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_04_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[405], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_04()
        if user_value(key='Round_04', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_05(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return Round_05_Random_01()
        if random_condition(rate=1):
            return Round_05_Random_02()
        if random_condition(rate=1):
            return Round_05_Random_03()
        if random_condition(rate=1):
            return Round_05_Random_04()


class Round_05_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[408], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_05_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[406], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_05_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[403], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_05_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[405], arg2=True, arg3=0)
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_06(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return Round_06_Random_01()
        if random_condition(rate=1):
            return Round_06_Random_02()
        if random_condition(rate=1):
            return Round_06_Random_03()
        if random_condition(rate=1):
            return Round_06_Random_04()


class Round_06_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[421], arg2=True, arg3=0)
        create_monster(spawnIds=[422], arg2=True, arg3=2000)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_06()
        if user_value(key='Round_06', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_06_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[423], arg2=True, arg3=0)
        create_monster(spawnIds=[424], arg2=True, arg3=2000)
        create_monster(spawnIds=[425], arg2=True, arg3=0)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_06()
        if user_value(key='Round_06', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_06_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[426], arg2=True, arg3=0)
        create_monster(spawnIds=[427], arg2=True, arg3=2000)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_06()
        if user_value(key='Round_06', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_06_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[428], arg2=True, arg3=0)
        create_monster(spawnIds=[429], arg2=True, arg3=2000)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_06()
        if user_value(key='Round_06', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class End(state.State):
    pass


