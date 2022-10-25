""" trigger/02020051_bf/106_summon_mob_2.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[1001], isStart=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Summon_monster_2', value=1):
            return 몬스터등장(self.ctx)


class 몬스터등장(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[1001], isStart=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 리셋(self.ctx)


class 리셋(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Summon_monster_2', value=2):
            return 대기(self.ctx)


initial_state = 대기
