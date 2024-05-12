""" trigger/02000303_bf/object_02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000591], state=0)
        self.set_interact_object(triggerIds=[10000592], state=0)
        self.set_interact_object(triggerIds=[10000593], state=0)
        self.set_interact_object(triggerIds=[10000594], state=0)
        self.set_interact_object(triggerIds=[10000595], state=0)
        self.set_effect(triggerIds=[60591], visible=False)
        self.set_effect(triggerIds=[60592], visible=False)
        self.set_effect(triggerIds=[60593], visible=False)
        self.set_effect(triggerIds=[60594], visible=False)
        self.set_effect(triggerIds=[60595], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 생성랜덤(self.ctx)


class 생성랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return 생성01(self.ctx)
        if self.random_condition(rate=20):
            return 생성02(self.ctx)
        if self.random_condition(rate=20):
            return 생성03(self.ctx)
        if self.random_condition(rate=20):
            return 생성04(self.ctx)
        if self.random_condition(rate=20):
            return 생성05(self.ctx)


class 생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000591], state=1)
        self.set_effect(triggerIds=[60591], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000591], stateValue=0):
            self.set_effect(triggerIds=[60591], visible=False)
            return 종료(self.ctx)


class 생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000592], state=1)
        self.set_effect(triggerIds=[60592], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000592], stateValue=0):
            self.set_effect(triggerIds=[60592], visible=False)
            return 종료(self.ctx)


class 생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000593], state=1)
        self.set_effect(triggerIds=[60593], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000593], stateValue=0):
            self.set_effect(triggerIds=[60593], visible=False)
            return 종료(self.ctx)


class 생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[60594], visible=True)
        self.set_interact_object(triggerIds=[10000594], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000594], stateValue=0):
            self.set_effect(triggerIds=[60594], visible=False)
            return 종료(self.ctx)


class 생성05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000595], state=1)
        self.set_effect(triggerIds=[60595], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000595], stateValue=0):
            self.set_effect(triggerIds=[60595], visible=False)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='120', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='120'):
            return 생성랜덤(self.ctx)


initial_state = 시작
