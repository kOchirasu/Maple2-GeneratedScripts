""" trigger/99999911/wave_projectile.xml """
import trigger_api


# 플레이어 감지
class Round_check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_01', value=1):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Round_03', value=1):
            return None # Missing State: Round_03
        if self.user_value(key='Round_04', value=1):
            return None # Missing State: Round_04


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
        if self.random_condition(weight=1):
            return Round_01_Random_05(self.ctx)
        if self.random_condition(weight=1):
            return Round_01_Random_06(self.ctx)


class Round_01_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=True)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)


class Round_01_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=True)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)


class Round_01_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[203], auto_target=True)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)


class Round_01_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[204], auto_target=True)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)


class Round_01_Random_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401], auto_target=True)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)


class Round_01_Random_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[402], auto_target=True)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Round_01(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)


class Round_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1):
            return Round_02_Random_01(self.ctx)
        if self.random_condition(weight=1):
            return Round_02_Random_02(self.ctx)
        if self.random_condition(weight=1):
            return Round_02_Random_03(self.ctx)
        if self.random_condition(weight=1):
            return Round_02_Random_04(self.ctx)
        if self.random_condition(weight=1):
            return Round_02_Random_05(self.ctx)
        if self.random_condition(weight=1):
            return Round_02_Random_06(self.ctx)


class Round_02_Random_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[202], auto_target=True, delay=2)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)


class Round_02_Random_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[201], auto_target=True, delay=2)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)


class Round_02_Random_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[203], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[204], auto_target=True, delay=2)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)


class Round_02_Random_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[204], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[203], auto_target=True, delay=2)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)


class Round_02_Random_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[401], auto_target=True, delay=2)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)


class Round_02_Random_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[402], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[402], auto_target=True, delay=2)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Round_02(self.ctx)
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)


initial_state = Round_check
