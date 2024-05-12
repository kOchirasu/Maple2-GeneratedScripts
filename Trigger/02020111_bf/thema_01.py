""" trigger/02020111_bf/thema_01.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1002]):
            return 소환준비(self.ctx)


class 소환준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 몬스터등장(self.ctx)


class 몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[141,142,143,144,145,146])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='monster_die', value=1):
            return 몬스터소멸(self.ctx)
        if self.monster_dead(spawn_ids=[141,142,143,144,145,146]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='monster_die', value=1):
            return 몬스터소멸(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return 몬스터등장(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[141,142,143,144,145,146])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakFail', value=1):
            return 시작(self.ctx)


initial_state = 시작
