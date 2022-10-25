""" trigger/02010026_bf/06_ladder14.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000909], state=1)
        self.set_ladder(triggerIds=[201], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[202], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[203], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[204], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[205], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[206], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[207], visible=False, animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000909], stateValue=0):
            return 사다리생성01(self.ctx)


class 사다리생성01(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[201], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return 사다리생성02(self.ctx)


class 사다리생성02(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[202], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return 사다리생성03(self.ctx)


class 사다리생성03(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[203], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return 사다리생성04(self.ctx)


class 사다리생성04(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[204], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return 사다리생성05(self.ctx)


class 사다리생성05(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[205], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return 사다리생성06(self.ctx)


class 사다리생성06(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[206], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return 사다리생성07(self.ctx)


class 사다리생성07(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[207], visible=True, animationEffect=True, animationDelay=5)
        self.set_timer(timerId='1', seconds=10, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
