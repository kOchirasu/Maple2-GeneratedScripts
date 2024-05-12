""" trigger/51000003_dg/wave_projectile.xml """
import trigger_api


# 플레이어 감지
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,298,299])
        self.destroy_monster(spawn_ids=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_01') >= 1:
            return Round_01_Ready(self.ctx)
        if self.user_value(key='Round_02') >= 1:
            return None # Missing State: Round_02_Ready
        if self.user_value(key='Round_03') >= 1:
            return None # Missing State: Round_03_Ready
        if self.user_value(key='Round_04') >= 1:
            return None # Missing State: Round_04_Ready
        if self.user_value(key='Round_05') >= 1:
            return None # Missing State: Round_05_Ready


class Round_01_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round_01(self.ctx)


class Round_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1):
            return Round_01_Random_01(self.ctx)
        if self.random_condition(weight=1):
            return Round_01_Random_02(self.ctx)
        if self.random_condition(weight=1):
            return Round_01_Random_03(self.ctx)
        if self.random_condition(weight=1):
            return Round_01_Random_04(self.ctx)
        if self.user_value(key='Round_02') >= 1:
            return Round_02(self.ctx)


class Round_01_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=True)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_01_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=True)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_01_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[203], auto_target=True)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_01_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[204], auto_target=True)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1):
            return Round_01_Random_01(self.ctx)
        if self.random_condition(weight=1):
            return Round_01_Random_02(self.ctx)
        if self.random_condition(weight=1):
            return Round_01_Random_03(self.ctx)
        if self.random_condition(weight=1):
            return Round_01_Random_04(self.ctx)
        if self.random_condition(weight=1):
            return Round_02_Random_01(self.ctx)
        if self.random_condition(weight=1):
            return Round_02_Random_02(self.ctx)
        if self.random_condition(weight=1):
            return Round_02_Random_03(self.ctx)
        if self.random_condition(weight=1):
            return Round_02_Random_04(self.ctx)


class Round_02_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[204], auto_target=True, delay=1000)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_02_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[203], auto_target=True, delay=1000)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_02_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[203], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[204], auto_target=True, delay=1000)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_02_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[202], auto_target=True, delay=1000)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_02_Random_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[204], auto_target=True, delay=1000)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_02_Random_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[403], auto_target=True, delay=1000)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1):
            return Round_03_Random_01(self.ctx)
        if self.random_condition(weight=1):
            return Round_03_Random_02(self.ctx)
        if self.random_condition(weight=1):
            return Round_03_Random_03(self.ctx)
        if self.random_condition(weight=1):
            return Round_03_Random_04(self.ctx)
        if self.random_condition(weight=1):
            return Round_03_Random_05(self.ctx)
        if self.random_condition(weight=1):
            return Round_03_Random_06(self.ctx)
        if self.random_condition(weight=1):
            return Round_03_Random_07(self.ctx)
        if self.random_condition(weight=1):
            return Round_03_Random_08(self.ctx)


class Round_03_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[205], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[206], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[207], auto_target=True, delay=4000)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_03_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[208], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[209], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[210], auto_target=True, delay=4000)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_03_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[205], auto_target=True, delay=4000)
        self.spawn_monster(spawn_ids=[206], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[207], auto_target=True, delay=0)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_03_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[208], auto_target=True, delay=4000)
        self.spawn_monster(spawn_ids=[209], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[210], auto_target=True, delay=0)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_03_Random_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[410], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[411], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[410], auto_target=True, delay=4000)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_03_Random_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[412], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[413], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[412], auto_target=True, delay=4000)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_03_Random_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[298], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[215], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[211], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[214], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[213], auto_target=True, delay=4000)
        self.spawn_monster(spawn_ids=[212], auto_target=True, delay=4000)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_03_Random_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[299], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[216], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[217], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[220], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[218], auto_target=True, delay=4000)
        self.spawn_monster(spawn_ids=[219], auto_target=True, delay=4000)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1):
            return Round_04_Random_01(self.ctx)
        if self.random_condition(weight=1):
            return Round_04_Random_02(self.ctx)
        if self.random_condition(weight=1):
            return Round_04_Random_03(self.ctx)
        if self.random_condition(weight=1):
            return Round_04_Random_04(self.ctx)
        if self.random_condition(weight=1):
            return Round_04_Random_05(self.ctx)
        if self.random_condition(weight=1):
            return Round_04_Random_06(self.ctx)
        if self.random_condition(weight=1):
            return Round_04_Random_07(self.ctx)
        if self.random_condition(weight=1):
            return Round_04_Random_08(self.ctx)


class Round_04_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[205], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[206], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[207], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[205], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_04_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[208], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[209], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[210], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[208], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_04_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[205], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[206], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[207], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[205], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_04_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[208], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[209], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[210], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[208], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_04_Random_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[410], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[411], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[410], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[410], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_04_Random_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[412], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[413], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[412], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[412], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_04_Random_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[298], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[215], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[211], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[214], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[213], auto_target=True, delay=4000)
        self.spawn_monster(spawn_ids=[212], auto_target=True, delay=4000)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_04_Random_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[299], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[216], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[217], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[220], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[218], auto_target=True, delay=4000)
        self.spawn_monster(spawn_ids=[219], auto_target=True, delay=4000)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1):
            return Round_05_Random_01(self.ctx)
        if self.random_condition(weight=1):
            return Round_05_Random_02(self.ctx)
        if self.random_condition(weight=1):
            return Round_05_Random_03(self.ctx)
        if self.random_condition(weight=1):
            return Round_05_Random_04(self.ctx)
        if self.random_condition(weight=1):
            return Round_05_Random_05(self.ctx)
        if self.random_condition(weight=1):
            return Round_05_Random_06(self.ctx)
        if self.random_condition(weight=1):
            return Round_05_Random_07(self.ctx)
        if self.random_condition(weight=1):
            return Round_05_Random_08(self.ctx)


class Round_05_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[205], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[206], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[207], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[205], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_05_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[208], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[209], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[210], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[208], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_05_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[205], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[206], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[207], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[205], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_05_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[208], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[209], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[210], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[208], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_05_Random_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[410], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[411], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[410], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[411], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_05_Random_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[412], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[413], auto_target=True, delay=1500)
        self.spawn_monster(spawn_ids=[412], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[413], auto_target=True, delay=4500)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_05_Random_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[298], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[215], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[211], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[214], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[213], auto_target=True, delay=4000)
        self.spawn_monster(spawn_ids=[212], auto_target=True, delay=4000)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_05_Random_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[299], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[216], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[217], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[220], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[218], auto_target=True, delay=4000)
        self.spawn_monster(spawn_ids=[219], auto_target=True, delay=4000)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05') >= 0:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=1, arg2='wave_projectile 종료', arg3='1000')
        pass


initial_state = Round_check
