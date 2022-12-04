""" trigger/02020051_bf/105_summon_mob.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[1003], isStart=True)
        self.start_combine_spawn(groupId=[1002], isStart=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon_monster', value=1):
            return 몬스터등장(self.ctx)


class 몬스터등장(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[1003], isStart=False)
        self.start_combine_spawn(groupId=[1002], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 리셋(self.ctx)


class 리셋(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon_monster', value=2):
            return 대기(self.ctx)


initial_state = 대기
