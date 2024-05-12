""" trigger/02000088_bf/fruit03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000140], state=1)
        self.set_effect(triggerIds=[203], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000140], stateValue=0):
            return 몬스터리젠(self.ctx)


class 몬스터리젠(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[203], visible=False)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대화(self.ctx)


class 대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103]):
            return 트리거초기화(self.ctx)
        if self.time_expired(timerId='1'):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.destroy_monster(spawnIds=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
