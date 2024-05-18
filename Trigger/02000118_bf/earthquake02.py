""" trigger/02000118_bf/earthquake02.xml """
import trigger_api


class 레버당기기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000291], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000291], state=0):
            return 스킬동작(self.ctx)


class 스킬동작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[2005], enable=True)
        self.set_skill(trigger_ids=[2006], enable=True)
        self.set_skill(trigger_ids=[2007], enable=True)
        self.set_skill(trigger_ids=[2008], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=10) # arg2는 시간 (초)
        self.set_skill(trigger_ids=[2005])
        self.set_skill(trigger_ids=[2006])
        self.set_skill(trigger_ids=[2007])
        self.set_skill(trigger_ids=[2008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 레버당기기(self.ctx)


initial_state = 레버당기기
