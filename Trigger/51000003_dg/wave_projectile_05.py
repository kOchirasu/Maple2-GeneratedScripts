""" trigger/51000003_dg/wave_projectile_05.xml """
import trigger_api


# 플레이어 감지
class Round_check(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[421,422,423,424,425,426,427,428,429,430])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_01', value=1):
            return Round_01_Ready(self.ctx)


class Round_01_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
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


class Round_01_Random_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[296], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[297], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[298], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[299], animationEffect=True, animationDelay=0)
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
    def on_enter(self):
        self.create_monster(spawnIds=[414], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_03', value=1):
            return None # Missing State: Round_03
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02_Random_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[415], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_03', value=1):
            return None # Missing State: Round_03
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02_Random_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[416], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_03', value=1):
            return None # Missing State: Round_03
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02_Random_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[417], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_03', value=1):
            return None # Missing State: Round_03
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class End(trigger_api.Trigger):
    pass


initial_state = Round_check
