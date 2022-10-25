""" trigger/02000088_bf/fruit01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000138], state=1)
        self.set_effect(triggerIds=[201], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000138], stateValue=0):
            return 몬스터리젠(self.ctx)


class 몬스터리젠(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[201], visible=False)
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대화(self.ctx)


class 대화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=90)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 트리거초기화(self.ctx)
        if self.time_expired(timerId='1'):
            return 트리거초기화(self.ctx)


class 트리거초기화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.destroy_monster(spawnIds=[101])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
