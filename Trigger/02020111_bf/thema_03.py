""" trigger/02020111_bf/thema_03.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1004]):
            return 소환준비(self.ctx)


class 소환준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 몬스터등장(self.ctx)


class 몬스터등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[161,162,163,164,165,166])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='monster_die', value=1):
            return 몬스터소멸(self.ctx)
        if self.monster_dead(boxIds=[161,162,163,164,165,166]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='monster_die', value=1):
            return 몬스터소멸(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 몬스터등장(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[161,162,163,164,165,166])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakFail', value=1):
            return 시작(self.ctx)


initial_state = 시작
