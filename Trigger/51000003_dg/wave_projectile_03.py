""" trigger/51000003_dg/wave_projectile_03.xml """
import common


# 플레이어 감지
class Round_check(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[421,422,423,424,425,426,427,428,429,430])

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Round_01', value=1):
            return Round_01_Ready(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return None # Missing State: Round_02
        if self.user_value(key='Round_03', value=1):
            return Round_03_Ready(self.ctx)
        if self.user_value(key='Round_04', value=1):
            return Round_04_Ready(self.ctx)
        if self.user_value(key='Round_05', value=1):
            return Round_05_Ready(self.ctx)
        if self.user_value(key='Round_06', value=1):
            return Round_06(self.ctx)


class Round_01_Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return Round_01(self.ctx)


class Round_02_Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return None # Missing State: Round_02


class Round_03_Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return Round_03(self.ctx)


class Round_04_Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return Round_04(self.ctx)


class Round_05_Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return Round_05(self.ctx)


class Round_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=1):
            return Round_01_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_01_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_01_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_01_Random_04(self.ctx)
        if self.random_condition(rate=1):
            return Round_01_Random_05(self.ctx)


class Round_01_Random_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[211], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[212], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[213], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[214], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_05(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[215], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=1):
            return Round_03_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_03_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_03_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_03_Random_04(self.ctx)


class Round_03_Random_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[408], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03_Random_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[406], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03_Random_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[403], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03_Random_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[405], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_03(self.ctx)
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=1):
            return Round_04_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_04_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_04_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_04_Random_04(self.ctx)


class Round_04_Random_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[408], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[406], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[403], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04_Random_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[405], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_04(self.ctx)
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=1):
            return Round_05_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_05_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_05_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_05_Random_04(self.ctx)


class Round_05_Random_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[408], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[406], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[403], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05_Random_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[405], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            return Round_05(self.ctx)
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_06(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=1):
            return Round_06_Random_01(self.ctx)
        if self.random_condition(rate=1):
            return Round_06_Random_02(self.ctx)
        if self.random_condition(rate=1):
            return Round_06_Random_03(self.ctx)
        if self.random_condition(rate=1):
            return Round_06_Random_04(self.ctx)


class Round_06_Random_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[421], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[422], animationEffect=True, animationDelay=2000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_06_Random_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[423], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[424], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[425], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_06_Random_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[426], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[427], animationEffect=True, animationDelay=2000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_06_Random_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[428], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[429], animationEffect=True, animationDelay=2000)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='7'):
            return Round_06(self.ctx)
        if self.user_value(key='Round_06', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class End(common.Trigger):
    pass


initial_state = Round_check
