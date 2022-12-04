""" trigger/02000303_bf/object_04.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000601], state=0)
        self.set_interact_object(triggerIds=[10000602], state=0)
        self.set_interact_object(triggerIds=[10000603], state=0)
        self.set_interact_object(triggerIds=[10000604], state=0)
        self.set_interact_object(triggerIds=[10000605], state=0)
        self.set_effect(triggerIds=[60601], visible=False)
        self.set_effect(triggerIds=[60602], visible=False)
        self.set_effect(triggerIds=[60603], visible=False)
        self.set_effect(triggerIds=[60604], visible=False)
        self.set_effect(triggerIds=[60605], visible=False)

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
        self.set_effect(triggerIds=[60601], visible=True)
        self.set_interact_object(triggerIds=[10000601], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000601], stateValue=0):
            self.set_effect(triggerIds=[60601], visible=False)
            return 종료(self.ctx)


class 생성02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60602], visible=True)
        self.set_interact_object(triggerIds=[10000602], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000602], stateValue=0):
            self.set_effect(triggerIds=[60602], visible=False)
            return 종료(self.ctx)


class 생성03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60603], visible=True)
        self.set_interact_object(triggerIds=[10000603], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000603], stateValue=0):
            self.set_effect(triggerIds=[60603], visible=False)
            return 종료(self.ctx)


class 생성04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60604], visible=True)
        self.set_interact_object(triggerIds=[10000604], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000604], stateValue=0):
            self.set_effect(triggerIds=[60604], visible=False)
            return 종료(self.ctx)


class 생성05(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60605], visible=True)
        self.set_interact_object(triggerIds=[10000605], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000605], stateValue=0):
            self.set_effect(triggerIds=[60605], visible=False)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='120', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='120'):
            return 생성랜덤(self.ctx)


initial_state = 시작
