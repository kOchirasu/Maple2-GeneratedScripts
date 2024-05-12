""" trigger/02020051_bf/105_summon_mob.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[1003], is_start=True)
        self.start_combine_spawn(group_id=[1002], is_start=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon_monster') >= 1:
            return 몬스터등장(self.ctx)


class 몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[1003], is_start=False)
        self.start_combine_spawn(group_id=[1002], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 리셋(self.ctx)


class 리셋(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon_monster') >= 2:
            return 대기(self.ctx)


initial_state = 대기
