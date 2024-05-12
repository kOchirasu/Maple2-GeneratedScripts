""" trigger/02000283_bf/heal07.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[707], enable=False)
        self.set_interact_object(triggerIds=[10000248], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000248], stateValue=0):
            return 스킬작동(self.ctx)


class 스킬작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[707], enable=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.set_skill(triggerIds=[707], enable=False)
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='29', seconds=29)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='29'):
            return 시작(self.ctx)


initial_state = 시작
