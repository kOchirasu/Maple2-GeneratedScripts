""" trigger/52000014_qd/rockdrop_1000.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1000], enable=False)
        self.set_skill(triggerIds=[1002], enable=False)
        self.set_skill(triggerIds=[1004], enable=False)
        self.set_effect(triggerIds=[1001], visible=False) # RockDrop
        self.set_effect(triggerIds=[1003], visible=False) # RockDrop
        self.set_effect(triggerIds=[1005], visible=False) # RockDrop

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 낙하01시작(self.ctx)


class 낙하01시작(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[1001], visible=True) # RockDrop

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return 낙하01완료(self.ctx)


class 낙하01완료(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1000], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return 낙하02시작(self.ctx)


class 낙하02시작(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[1003], visible=True) # RockDrop

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return 낙하02완료(self.ctx)


class 낙하02완료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=2)
        self.set_skill(triggerIds=[1002], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 낙하03시작(self.ctx)


class 낙하03시작(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[1005], visible=True) # RockDrop

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return 낙하03완료(self.ctx)


class 낙하03완료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=1)
        self.set_skill(triggerIds=[1004], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='4'):
            return 초기화(self.ctx)


class 초기화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=2)
        self.set_skill(triggerIds=[1000], enable=False)
        self.set_skill(triggerIds=[1002], enable=False)
        self.set_skill(triggerIds=[1004], enable=False)
        self.set_effect(triggerIds=[1001], visible=False) # RockDrop
        self.set_effect(triggerIds=[1003], visible=False) # RockDrop
        self.set_effect(triggerIds=[1005], visible=False) # RockDrop

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 낙하01시작(self.ctx)


initial_state = 대기
