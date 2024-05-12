""" trigger/51000003_dg/wave_projectile.xml """
import trigger_api


# 플레이어 감지
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,298,299])
        self.destroy_monster(spawnIds=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_01', value=1):
            return Round_01_Ready(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return None # Missing State: Round_02_Ready
        if self.user_value(key='Round_03', value=1):
            return None # Missing State: Round_03_Ready
        if self.user_value(key='Round_04', value=1):
            return None # Missing State: Round_04_Ready
        if self.user_value(key='Round_05', value=1):
            return None # Missing State: Round_05_Ready


class Round_01_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round_01(self.ctx)


class Round_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return Round_01_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_01_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_01_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_01_Random_04(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)


class Round_01_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[203], animationEffect=True)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[204], animationEffect=True)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return Round_01_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_01_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_01_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_01_Random_04(self.ctx)
        if self.random_condition(rate=1):
            return Round_02_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_02_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_02_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_02_Random_04(self.ctx)


class Round_02_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[201], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[204], animationEffect=True, animationDelay=1000)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[202], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[203], animationEffect=True, animationDelay=1000)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[203], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[204], animationEffect=True, animationDelay=1000)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[201], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[202], animationEffect=True, animationDelay=1000)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02_Random_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[202], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[204], animationEffect=True, animationDelay=1000)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02_Random_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[401], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[403], animationEffect=True, animationDelay=1000)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return Round_03_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_03_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_03_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_03_Random_04(self.ctx)
        if self.random_condition(rate=1):
            return Round_03_Random_05(self.ctx)
        if self.random_condition(rate=1):
            return Round_03_Random_06(self.ctx)
        if self.random_condition(rate=1):
            return Round_03_Random_07(self.ctx)
        if self.random_condition(rate=1):
            return Round_03_Random_08(self.ctx)


class Round_03_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[205], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[206], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[207], animationEffect=True, animationDelay=4000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[208], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[209], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[210], animationEffect=True, animationDelay=4000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[205], animationEffect=True, animationDelay=4000)
        self.create_monster(spawnIds=[206], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[207], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[208], animationEffect=True, animationDelay=4000)
        self.create_monster(spawnIds=[209], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[210], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03_Random_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[410], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[411], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[410], animationEffect=True, animationDelay=4000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03_Random_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[412], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[413], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[412], animationEffect=True, animationDelay=4000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03_Random_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[298], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[215], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[211], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[214], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[213], animationEffect=True, animationDelay=4000)
        self.create_monster(spawnIds=[212], animationEffect=True, animationDelay=4000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03_Random_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[299], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[216], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[217], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[220], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[218], animationEffect=True, animationDelay=4000)
        self.create_monster(spawnIds=[219], animationEffect=True, animationDelay=4000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return Round_04_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_04_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_04_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_04_Random_04(self.ctx)
        if self.random_condition(rate=1):
            return Round_04_Random_05(self.ctx)
        if self.random_condition(rate=1):
            return Round_04_Random_06(self.ctx)
        if self.random_condition(rate=1):
            return Round_04_Random_07(self.ctx)
        if self.random_condition(rate=1):
            return Round_04_Random_08(self.ctx)


class Round_04_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[205], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[206], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[207], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[205], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[208], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[209], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[210], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[208], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[205], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[206], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[207], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[205], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[208], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[209], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[210], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[208], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[410], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[411], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[410], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[410], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[412], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[413], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[412], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[412], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[298], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[215], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[211], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[214], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[213], animationEffect=True, animationDelay=4000)
        self.create_monster(spawnIds=[212], animationEffect=True, animationDelay=4000)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[299], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[216], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[217], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[220], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[218], animationEffect=True, animationDelay=4000)
        self.create_monster(spawnIds=[219], animationEffect=True, animationDelay=4000)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return Round_05_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_05_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_05_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_05_Random_04(self.ctx)
        if self.random_condition(rate=1):
            return Round_05_Random_05(self.ctx)
        if self.random_condition(rate=1):
            return Round_05_Random_06(self.ctx)
        if self.random_condition(rate=1):
            return Round_05_Random_07(self.ctx)
        if self.random_condition(rate=1):
            return Round_05_Random_08(self.ctx)


class Round_05_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[205], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[206], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[207], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[205], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[208], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[209], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[210], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[208], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[205], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[206], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[207], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[205], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[208], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[209], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[210], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[208], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[410], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[411], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[410], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[411], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[412], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[413], animationEffect=True, animationDelay=1500)
        self.create_monster(spawnIds=[412], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[413], animationEffect=True, animationDelay=4500)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[298], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[215], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[211], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[214], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[213], animationEffect=True, animationDelay=4000)
        self.create_monster(spawnIds=[212], animationEffect=True, animationDelay=4000)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[299], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[216], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[217], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[220], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[218], animationEffect=True, animationDelay=4000)
        self.create_monster(spawnIds=[219], animationEffect=True, animationDelay=4000)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=1, arg2='wave_projectile 종료', arg3='1000')
        pass


initial_state = Round_check
