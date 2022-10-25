""" trigger/02000325_bf/heal02.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[702], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000740], stateValue=0):
            return 스킬작동(self.ctx)


class 스킬작동(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[702], enable=True)
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[612], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            self.set_skill(triggerIds=[702], enable=False)
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            self.set_interact_object(triggerIds=[10000740], state=2)
            return 시작(self.ctx)


initial_state = 시작
