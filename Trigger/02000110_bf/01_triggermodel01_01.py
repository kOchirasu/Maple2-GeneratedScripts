""" trigger/02000110_bf/01_triggermodel01_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000063], state=1)
        self.set_actor(triggerId=10, visible=True, initialSequence='Closed')
        self.set_effect(triggerIds=[201], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000063], stateValue=0):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=10, visible=True, initialSequence='Opened')
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.set_effect(triggerIds=[201], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 몬스터전투(self.ctx)


class 몬스터전투(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(boxIds=[101]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[101]):
            self.reset_timer(timerId='1')
            return None
        if self.monster_dead(boxIds=[101]):
            return 소멸대기(self.ctx)
        if self.time_expired(timerId='1'):
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 트리거초기화(self.ctx)
        if self.monster_in_combat(boxIds=[101]):
            return 몬스터소멸(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.set_timer(timerId='2', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 대기(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='2')


initial_state = 대기
