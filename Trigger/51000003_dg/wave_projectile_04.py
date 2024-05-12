""" trigger/51000003_dg/wave_projectile_04.xml """
import trigger_api


# 플레이어 감지
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
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
        if self.random_condition(rate=1):
            return Round_01_Random_05(self.ctx)


class Round_01_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[216], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[217], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[218], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[219], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_01_Random_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[220], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='9', seconds=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=1, arg2='wave_projectile_04 종료', arg3='1000')
        pass


initial_state = Round_check
