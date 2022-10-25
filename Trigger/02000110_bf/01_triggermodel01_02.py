""" trigger/02000110_bf/01_triggermodel01_02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000064], state=1)
        self.set_actor(triggerId=11, visible=True, initialSequence='Closed')
        self.set_effect(triggerIds=[202], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000064], stateValue=0):
            return 몬스터와전투(self.ctx)


class 몬스터와전투(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=11, visible=True, initialSequence='Opened')
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.set_effect(triggerIds=[202], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 몬스터전투(self.ctx)


class 몬스터전투(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[102]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(boxIds=[102]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[102]):
            self.reset_timer(timerId='1')
            return None
        if self.monster_dead(boxIds=[102]):
            return 소멸대기(self.ctx)
        if self.time_expired(timerId='1'):
            return 소멸대기(self.ctx)


class 소멸대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 트리거초기화(self.ctx)
        if self.monster_in_combat(boxIds=[102]):
            return 몬스터소멸(self.ctx)


class 트리거초기화(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])
        self.set_timer(timerId='2', seconds=20)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 대기(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='2')


initial_state = 대기
