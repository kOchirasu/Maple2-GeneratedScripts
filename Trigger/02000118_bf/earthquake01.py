""" trigger/02000118_bf/earthquake01.xml """
import trigger_api


class 레버당기기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000290], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000290], stateValue=0):
            return 스킬동작(self.ctx)


class 스킬동작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2001], enable=True)
        self.set_skill(triggerIds=[2002], enable=True)
        self.set_skill(triggerIds=[2003], enable=True)
        self.set_skill(triggerIds=[2004], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=10) # arg2는 시간 (초)
        self.set_skill(triggerIds=[2001], enable=False)
        self.set_skill(triggerIds=[2002], enable=False)
        self.set_skill(triggerIds=[2003], enable=False)
        self.set_skill(triggerIds=[2004], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 레버당기기(self.ctx)


initial_state = 레버당기기
