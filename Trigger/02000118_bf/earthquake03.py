""" trigger/02000118_bf/earthquake03.xml """
import common


class 레버당기기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000292], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000292], stateValue=0):
            return 스킬동작(self.ctx)


class 스킬동작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[2009], enable=True)
        self.set_skill(triggerIds=[2010], enable=True)
        self.set_skill(triggerIds=[2011], enable=True)
        self.set_skill(triggerIds=[2012], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=10) # arg2는 시간 (초)
        self.set_skill(triggerIds=[2009], enable=False)
        self.set_skill(triggerIds=[2010], enable=False)
        self.set_skill(triggerIds=[2011], enable=False)
        self.set_skill(triggerIds=[2012], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 레버당기기(self.ctx)


initial_state = 레버당기기
