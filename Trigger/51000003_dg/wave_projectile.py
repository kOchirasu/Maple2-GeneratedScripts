""" trigger/51000003_dg/wave_projectile.xml """
from common import *
import state


#  플레이어 감지 
class Round_check(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,298,299])
        destroy_monster(spawnIds=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417])

    def on_tick(self) -> state.State:
        if user_value(key='Round_01', value=1):
            return Round_01_Ready()
        if user_value(key='Round_02', value=1):
            return None # Missing State: Round_02_Ready
        if user_value(key='Round_03', value=1):
            return None # Missing State: Round_03_Ready
        if user_value(key='Round_04', value=1):
            return None # Missing State: Round_04_Ready
        if user_value(key='Round_05', value=1):
            return None # Missing State: Round_05_Ready


class Round_01_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
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
        if user_value(key='Round_02', value=1):
            return Round_02()


class Round_01_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_01_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=True)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_01_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[203], arg2=True)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_01_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=True)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Round_01()
        if user_value(key='Round_01', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_02(state.State):
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
            return Round_02_Random_01()
        if random_condition(rate=1):
            return Round_02_Random_02()
        if random_condition(rate=1):
            return Round_02_Random_03()
        if random_condition(rate=1):
            return Round_02_Random_04()


class Round_02_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True, arg3=0)
        create_monster(spawnIds=[204], arg2=True, arg3=1000)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Round_02()
        if user_value(key='Round_02', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_02_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=True, arg3=0)
        create_monster(spawnIds=[203], arg2=True, arg3=1000)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Round_02()
        if user_value(key='Round_02', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_02_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[203], arg2=True, arg3=0)
        create_monster(spawnIds=[204], arg2=True, arg3=1000)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Round_02()
        if user_value(key='Round_02', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_02_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True, arg3=0)
        create_monster(spawnIds=[202], arg2=True, arg3=1000)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Round_02()
        if user_value(key='Round_02', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_02_Random_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=True, arg3=0)
        create_monster(spawnIds=[204], arg2=True, arg3=1000)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Round_02()
        if user_value(key='Round_02', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_02_Random_06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401], arg2=True, arg3=0)
        create_monster(spawnIds=[403], arg2=True, arg3=1000)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Round_02()
        if user_value(key='Round_02', value=0):
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
        if random_condition(rate=1):
            return Round_03_Random_05()
        if random_condition(rate=1):
            return Round_03_Random_06()
        if random_condition(rate=1):
            return Round_03_Random_07()
        if random_condition(rate=1):
            return Round_03_Random_08()


class Round_03_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True, arg3=0)
        create_monster(spawnIds=[206], arg2=True, arg3=2000)
        create_monster(spawnIds=[207], arg2=True, arg3=4000)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_03()
        if user_value(key='Round_03', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_03_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[208], arg2=True, arg3=0)
        create_monster(spawnIds=[209], arg2=True, arg3=2000)
        create_monster(spawnIds=[210], arg2=True, arg3=4000)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_03()
        if user_value(key='Round_03', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_03_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True, arg3=4000)
        create_monster(spawnIds=[206], arg2=True, arg3=2000)
        create_monster(spawnIds=[207], arg2=True, arg3=0)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_03()
        if user_value(key='Round_03', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_03_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[208], arg2=True, arg3=4000)
        create_monster(spawnIds=[209], arg2=True, arg3=2000)
        create_monster(spawnIds=[210], arg2=True, arg3=0)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_03()
        if user_value(key='Round_03', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_03_Random_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[410], arg2=True, arg3=0)
        create_monster(spawnIds=[411], arg2=True, arg3=2000)
        create_monster(spawnIds=[410], arg2=True, arg3=4000)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_03()
        if user_value(key='Round_03', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_03_Random_06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[412], arg2=True, arg3=0)
        create_monster(spawnIds=[413], arg2=True, arg3=2000)
        create_monster(spawnIds=[412], arg2=True, arg3=4000)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_03()
        if user_value(key='Round_03', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_03_Random_07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[298], arg2=True, arg3=0)
        create_monster(spawnIds=[215], arg2=True, arg3=0)
        create_monster(spawnIds=[211], arg2=True, arg3=2000)
        create_monster(spawnIds=[214], arg2=True, arg3=2000)
        create_monster(spawnIds=[213], arg2=True, arg3=4000)
        create_monster(spawnIds=[212], arg2=True, arg3=4000)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_03()
        if user_value(key='Round_03', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_03_Random_08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[299], arg2=True, arg3=0)
        create_monster(spawnIds=[216], arg2=True, arg3=0)
        create_monster(spawnIds=[217], arg2=True, arg3=2000)
        create_monster(spawnIds=[220], arg2=True, arg3=2000)
        create_monster(spawnIds=[218], arg2=True, arg3=4000)
        create_monster(spawnIds=[219], arg2=True, arg3=4000)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
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
        if random_condition(rate=1):
            return Round_04_Random_05()
        if random_condition(rate=1):
            return Round_04_Random_06()
        if random_condition(rate=1):
            return Round_04_Random_07()
        if random_condition(rate=1):
            return Round_04_Random_08()


class Round_04_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True, arg3=0)
        create_monster(spawnIds=[206], arg2=True, arg3=1500)
        create_monster(spawnIds=[207], arg2=True, arg3=3000)
        create_monster(spawnIds=[205], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_04()
        if user_value(key='Round_04', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_04_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[208], arg2=True, arg3=0)
        create_monster(spawnIds=[209], arg2=True, arg3=1500)
        create_monster(spawnIds=[210], arg2=True, arg3=3000)
        create_monster(spawnIds=[208], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_04()
        if user_value(key='Round_04', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_04_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True, arg3=3000)
        create_monster(spawnIds=[206], arg2=True, arg3=1500)
        create_monster(spawnIds=[207], arg2=True, arg3=0)
        create_monster(spawnIds=[205], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_04()
        if user_value(key='Round_04', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_04_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[208], arg2=True, arg3=3000)
        create_monster(spawnIds=[209], arg2=True, arg3=1500)
        create_monster(spawnIds=[210], arg2=True, arg3=0)
        create_monster(spawnIds=[208], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_04()
        if user_value(key='Round_04', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_04_Random_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[410], arg2=True, arg3=0)
        create_monster(spawnIds=[411], arg2=True, arg3=1500)
        create_monster(spawnIds=[410], arg2=True, arg3=3000)
        create_monster(spawnIds=[410], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_04()
        if user_value(key='Round_04', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_04_Random_06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[412], arg2=True, arg3=0)
        create_monster(spawnIds=[413], arg2=True, arg3=1500)
        create_monster(spawnIds=[412], arg2=True, arg3=3000)
        create_monster(spawnIds=[412], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_04()
        if user_value(key='Round_04', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_04_Random_07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[298], arg2=True, arg3=0)
        create_monster(spawnIds=[215], arg2=True, arg3=0)
        create_monster(spawnIds=[211], arg2=True, arg3=2000)
        create_monster(spawnIds=[214], arg2=True, arg3=2000)
        create_monster(spawnIds=[213], arg2=True, arg3=4000)
        create_monster(spawnIds=[212], arg2=True, arg3=4000)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return Round_04()
        if user_value(key='Round_04', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_04_Random_08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[299], arg2=True, arg3=0)
        create_monster(spawnIds=[216], arg2=True, arg3=0)
        create_monster(spawnIds=[217], arg2=True, arg3=2000)
        create_monster(spawnIds=[220], arg2=True, arg3=2000)
        create_monster(spawnIds=[218], arg2=True, arg3=4000)
        create_monster(spawnIds=[219], arg2=True, arg3=4000)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
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
        if random_condition(rate=1):
            return Round_05_Random_05()
        if random_condition(rate=1):
            return Round_05_Random_06()
        if random_condition(rate=1):
            return Round_05_Random_07()
        if random_condition(rate=1):
            return Round_05_Random_08()


class Round_05_Random_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True, arg3=0)
        create_monster(spawnIds=[206], arg2=True, arg3=1500)
        create_monster(spawnIds=[207], arg2=True, arg3=3000)
        create_monster(spawnIds=[205], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_05_Random_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[208], arg2=True, arg3=0)
        create_monster(spawnIds=[209], arg2=True, arg3=1500)
        create_monster(spawnIds=[210], arg2=True, arg3=3000)
        create_monster(spawnIds=[208], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_05_Random_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True, arg3=3000)
        create_monster(spawnIds=[206], arg2=True, arg3=1500)
        create_monster(spawnIds=[207], arg2=True, arg3=0)
        create_monster(spawnIds=[205], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_05_Random_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[208], arg2=True, arg3=3000)
        create_monster(spawnIds=[209], arg2=True, arg3=1500)
        create_monster(spawnIds=[210], arg2=True, arg3=0)
        create_monster(spawnIds=[208], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_05_Random_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[410], arg2=True, arg3=0)
        create_monster(spawnIds=[411], arg2=True, arg3=1500)
        create_monster(spawnIds=[410], arg2=True, arg3=3000)
        create_monster(spawnIds=[411], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_05_Random_06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[412], arg2=True, arg3=0)
        create_monster(spawnIds=[413], arg2=True, arg3=1500)
        create_monster(spawnIds=[412], arg2=True, arg3=3000)
        create_monster(spawnIds=[413], arg2=True, arg3=4500)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_05_Random_07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[298], arg2=True, arg3=0)
        create_monster(spawnIds=[215], arg2=True, arg3=0)
        create_monster(spawnIds=[211], arg2=True, arg3=2000)
        create_monster(spawnIds=[214], arg2=True, arg3=2000)
        create_monster(spawnIds=[213], arg2=True, arg3=4000)
        create_monster(spawnIds=[212], arg2=True, arg3=4000)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_05_Random_08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[299], arg2=True, arg3=0)
        create_monster(spawnIds=[216], arg2=True, arg3=0)
        create_monster(spawnIds=[217], arg2=True, arg3=2000)
        create_monster(spawnIds=[220], arg2=True, arg3=2000)
        create_monster(spawnIds=[218], arg2=True, arg3=4000)
        create_monster(spawnIds=[219], arg2=True, arg3=4000)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return Round_05()
        if user_value(key='Round_05', value=0):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class End(state.State):
    pass


