""" trigger/66000004_gd/buffskill_03.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=203, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10603]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=203, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[10603]):
            return 초기화(self.ctx)
        if self.random_condition(rate=33):
            return A스킬작동(self.ctx)
        if self.random_condition(rate=33):
            return B스킬작동(self.ctx)
        if self.random_condition(rate=34):
            return C스킬작동(self.ctx)


class A스킬작동(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7301], enable=True)
        self.set_timer(timerId='60', seconds=60)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='60'):
            self.set_skill(triggerIds=[7301], enable=False)
            return 시작대기중(self.ctx)


class B스킬작동(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7302], enable=True)
        self.set_timer(timerId='60', seconds=60)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='60'):
            self.set_skill(triggerIds=[7302], enable=False)
            return 시작대기중(self.ctx)


class C스킬작동(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7303], enable=True)
        self.set_timer(timerId='60', seconds=60)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='60'):
            self.set_skill(triggerIds=[7303], enable=False)
            return 시작대기중(self.ctx)


class 초기화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[7301], enable=False)
        self.set_skill(triggerIds=[7302], enable=False)
        self.set_skill(triggerIds=[7303], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
