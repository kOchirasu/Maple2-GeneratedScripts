""" trigger/02000303_bf/object_01.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000586], state=0)
        self.set_interact_object(triggerIds=[10000587], state=0)
        self.set_interact_object(triggerIds=[10000588], state=0)
        self.set_interact_object(triggerIds=[10000589], state=0)
        self.set_interact_object(triggerIds=[10000590], state=0)
        self.set_effect(triggerIds=[60586], visible=False)
        self.set_effect(triggerIds=[60587], visible=False)
        self.set_effect(triggerIds=[60588], visible=False)
        self.set_effect(triggerIds=[60589], visible=False)
        self.set_effect(triggerIds=[60590], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 생성랜덤(self.ctx)


class 생성랜덤(common.Trigger):
    def on_tick(self) -> common.Trigger:
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


class 생성01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60586], visible=True)
        self.set_interact_object(triggerIds=[10000586], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000586], stateValue=0):
            self.set_effect(triggerIds=[60586], visible=False)
            return 종료(self.ctx)


class 생성02(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000587], state=1)
        self.set_effect(triggerIds=[60587], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000587], stateValue=0):
            self.set_effect(triggerIds=[60587], visible=False)
            return 종료(self.ctx)


class 생성03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60588], visible=True)
        self.set_interact_object(triggerIds=[10000588], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000588], stateValue=0):
            self.set_effect(triggerIds=[60588], visible=False)
            return 종료(self.ctx)


class 생성04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60589], visible=True)
        self.set_interact_object(triggerIds=[10000589], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000589], stateValue=0):
            self.set_effect(triggerIds=[60589], visible=False)
            return 종료(self.ctx)


class 생성05(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[60590], visible=True)
        self.set_interact_object(triggerIds=[10000590], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000590], stateValue=0):
            self.set_effect(triggerIds=[60590], visible=False)
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='120', seconds=120)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='120'):
            return 생성랜덤(self.ctx)


initial_state = 시작
