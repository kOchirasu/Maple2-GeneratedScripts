""" trigger/02000281_bf/heal03.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[703], enable=False)
        self.set_interact_object(trigger_ids=[10000252], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000252], state=0):
            return 스킬작동(self.ctx)


class 스킬작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[703], enable=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.set_skill(trigger_ids=[703], enable=False)
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='29', seconds=29)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='29'):
            return 시작(self.ctx)


initial_state = 시작
