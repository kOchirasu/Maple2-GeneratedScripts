""" trigger/02000090_bf/apply_01.xml """
import trigger_api


class 대기0(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[1000], visible=False)
        self.set_effect(triggerIds=[1001], visible=False)
        self.set_interact_object(triggerIds=[10000360], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=33):
            return 대기1(self.ctx)
        if self.random_condition(rate=33):
            return 대기2(self.ctx)
        if self.random_condition(rate=34):
            return 대기3(self.ctx)
        if self.object_interacted(interactIds=[10000360], stateValue=0):
            return 이펙트1(self.ctx)


class 대기1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)
        self.set_effect(triggerIds=[1000], visible=True)
        self.set_interact_object(triggerIds=[10000360], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기0(self.ctx)
        if self.object_interacted(interactIds=[10000360], stateValue=0):
            return 이펙트1(self.ctx)


class 대기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=7)
        self.set_effect(triggerIds=[1000], visible=True)
        self.set_effect(triggerIds=[1001], visible=True)
        self.set_interact_object(triggerIds=[10000360], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 대기0(self.ctx)
        if self.object_interacted(interactIds=[10000360], stateValue=0):
            return 이펙트1(self.ctx)


class 대기3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=1)
        self.set_effect(triggerIds=[1000], visible=True)
        self.set_effect(triggerIds=[1001], visible=True)
        self.set_interact_object(triggerIds=[10000360], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 대기0(self.ctx)
        if self.object_interacted(interactIds=[10000360], stateValue=0):
            return 이펙트1(self.ctx)


class 이펙트1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=1)
        self.set_effect(triggerIds=[1000], visible=True)
        self.set_effect(triggerIds=[1001], visible=True)
        self.set_effect(triggerIds=[2000], visible=True)
        self.set_effect(triggerIds=[2001], visible=True)
        self.set_effect(triggerIds=[2002], visible=True)
        self.set_effect(triggerIds=[2003], visible=True)
        self.set_effect(triggerIds=[2004], visible=True)
        self.set_effect(triggerIds=[2005], visible=True)
        self.set_effect(triggerIds=[2006], visible=True)
        self.set_effect(triggerIds=[2007], visible=True)
        self.set_effect(triggerIds=[1000], visible=False)
        self.set_effect(triggerIds=[1001], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[1000], visible=False)
        self.set_effect(triggerIds=[1001], visible=False)
        self.set_effect(triggerIds=[2000], visible=False)
        self.set_effect(triggerIds=[2001], visible=False)
        self.set_effect(triggerIds=[2002], visible=False)
        self.set_effect(triggerIds=[2003], visible=False)
        self.set_effect(triggerIds=[2004], visible=False)
        self.set_timer(timerId='20', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='20'):
            return 대기0(self.ctx)


initial_state = 대기0
