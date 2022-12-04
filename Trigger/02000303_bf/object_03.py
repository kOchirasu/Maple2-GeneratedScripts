""" trigger/02000303_bf/object_03.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000596], state=0)
        self.set_interact_object(triggerIds=[10000597], state=0)
        self.set_interact_object(triggerIds=[10000598], state=0)
        self.set_interact_object(triggerIds=[10000599], state=0)
        self.set_interact_object(triggerIds=[10000600], state=0)
        self.set_effect(triggerIds=[60596], visible=False)
        self.set_effect(triggerIds=[60597], visible=False)
        self.set_effect(triggerIds=[60598], visible=False)
        self.set_effect(triggerIds=[60599], visible=False)
        self.set_effect(triggerIds=[60600], visible=False)

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
    def on_enter(self):
        self.set_effect(triggerIds=[60596], visible=True)
        self.set_interact_object(triggerIds=[10000596], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000596], stateValue=0):
            self.set_effect(triggerIds=[60596], visible=False)
            return 종료(self.ctx)


class 생성02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60597], visible=True)
        self.set_interact_object(triggerIds=[10000597], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000597], stateValue=0):
            self.set_effect(triggerIds=[60597], visible=False)
            return 종료(self.ctx)


class 생성03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60598], visible=True)
        self.set_interact_object(triggerIds=[10000598], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000598], stateValue=0):
            self.set_effect(triggerIds=[60598], visible=False)
            return 종료(self.ctx)


class 생성04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60599], visible=True)
        self.set_interact_object(triggerIds=[10000599], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000599], stateValue=0):
            self.set_effect(triggerIds=[60599], visible=False)
            return 종료(self.ctx)


class 생성05(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60600], visible=True)
        self.set_interact_object(triggerIds=[10000600], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000600], stateValue=0):
            self.set_effect(triggerIds=[60600], visible=False)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='120', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='120'):
            return 생성랜덤(self.ctx)


initial_state = 시작
