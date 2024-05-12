""" trigger/02000110_bf/01_triggermodel01_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000065], state=1)
        self.set_actor(trigger_id=12, visible=True, initial_sequence='Closed')
        self.set_effect(trigger_ids=[203], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000065], state=0):
            return 몬스터와전투(self.ctx)


class 몬스터와전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=12, visible=True, initial_sequence='Opened')
        self.spawn_monster(spawn_ids=[103], auto_target=True)
        self.set_effect(trigger_ids=[203], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 몬스터전투(self.ctx)


class 몬스터전투(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(spawn_ids=[103]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[103]):
            self.reset_timer(timer_id='1')
        if self.monster_dead(spawn_ids=[103]):
            return 소멸대기(self.ctx)
        if self.time_expired(timer_id='1'):
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 트리거초기화(self.ctx)
        if self.monster_in_combat(spawn_ids=[103]):
            return 몬스터소멸(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[103])
        self.set_timer(timer_id='2', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 대기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='2')


initial_state = 대기
