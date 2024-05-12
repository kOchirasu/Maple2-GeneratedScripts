""" trigger/51000003_dg/wave_projectile_02.xml """
import trigger_api


# 플레이어 감지
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[421,422,423,424,425,426,427,428,429,430])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_00', value=1):
            return Round_00_Ready(self.ctx)
        if self.user_value(key='Round_01', value=1):
            return Round_01_Ready(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Round_03', value=1):
            return Round_03_Ready(self.ctx)
        if self.user_value(key='Round_04', value=1):
            return Round_04_Ready(self.ctx)
        if self.user_value(key='Round_05', value=1):
            return Round_05_Ready(self.ctx)


class Round_00_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return Round_00(self.ctx)


class Round_01_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return Round_01(self.ctx)


class Round_03_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return None # Missing State: Round_03


class Round_04_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return Round_04(self.ctx)


class Round_05_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return Round_05(self.ctx)


class Round_00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return Round_00_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_00_Random_02(self.ctx)


class Round_00_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[403], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_00(self.ctx)
        if self.user_value(key='Round_01', value=1):
            return Round_01(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_00_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[404], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_00(self.ctx)
        if self.user_value(key='Round_01', value=1):
            return Round_01(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


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


class Round_01_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[401], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[402], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[403], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[404], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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
        self.create_monster(spawnIds=[405,406], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[407,408], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[410,411], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[412,413], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
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


class Round_04_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[408], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[406], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[403], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[405], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
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


class Round_05_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[408], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[406], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[403], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[405], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return Round_06_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_06_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_06_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_06_Random_04(self.ctx)


class Round_06_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[421], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[422], animationEffect=True, animationDelay=2000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_06_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[423], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[424], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[425], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_06_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[426], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[427], animationEffect=True, animationDelay=2000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_06_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[428], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[429], animationEffect=True, animationDelay=2000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=1, arg2='wave_projectile_02 종료', arg3='1000')
        pass


initial_state = Round_check
