""" trigger/02000139_bf/01_trigger01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[401,402,403,404], visible=False)
        self.set_interact_object(triggerIds=[10000131], state=1)
        self.set_mesh(triggerIds=[201,202,203], visible=False)
        self.set_ladder(triggerIds=[301], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[302], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[303], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[304], visible=False, animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000131], stateValue=0):
            return 발판등장1(self.ctx)


class 발판등장1(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[201], visible=True)
        self.set_timer(timerId='2', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 발판등장2(self.ctx)


class 발판등장2(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[202], visible=True)
        self.set_timer(timerId='3', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 발판등장3(self.ctx)


class 발판등장3(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[203], visible=True)
        self.set_timer(timerId='4', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='4'):
            return 사다리등장(self.ctx)


class 사다리등장(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[301], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[401], visible=True)
        self.set_ladder(triggerIds=[302], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[402], visible=True)
        self.set_ladder(triggerIds=[303], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[403], visible=True)
        self.set_ladder(triggerIds=[304], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[404], visible=True)
        self.set_timer(timerId='4', seconds=20)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='4'):
            return 대기(self.ctx)


initial_state = 대기
