""" trigger/02000282_bf/heal06.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[706], enable=False)
        self.set_interact_object(triggerIds=[10000249], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000249], stateValue=0):
            return 스킬작동(self.ctx)


class 스킬작동(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[706], enable=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            self.set_skill(triggerIds=[706], enable=False)
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='29', seconds=29)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='29'):
            return 시작(self.ctx)


initial_state = 시작
