""" trigger/02020111_bf/thema_04.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1005]):
            return 소환준비(self.ctx)


class 소환준비(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 몬스터등장(self.ctx)


class 몬스터등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[171,172,173,174,175,176])

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='monster_die', value=1):
            return 몬스터소멸(self.ctx)
        if self.monster_dead(boxIds=[171,172,173,174,175,176]):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='monster_die', value=1):
            return 몬스터소멸(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 몬스터등장(self.ctx)


class 몬스터소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[171,172,173,174,175,176])

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SkillBreakFail', value=1):
            return 시작(self.ctx)


initial_state = 시작
