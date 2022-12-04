""" trigger/02000014_ad/01_ladder.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000066], state=1)
        self.set_effect(triggerIds=[201,202,211,212,221,222,231,232,241,242], visible=False)
        self.set_ladder(triggerIds=[101], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[102], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[111], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[112], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[121], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[122], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[131], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[132], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[141], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[142], visible=False, animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000066], stateValue=0):
            return 사다리생성101(self.ctx)


class 사다리생성101(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[201,202], visible=True)
        self.set_ladder(triggerIds=[101], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[102], visible=True, animationEffect=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 사다리생성102(self.ctx)


class 사다리생성102(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[211,212], visible=True)
        self.set_ladder(triggerIds=[111], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[112], visible=True, animationEffect=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 사다리생성111(self.ctx)


class 사다리생성111(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[221,222], visible=True)
        self.set_ladder(triggerIds=[121], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[122], visible=True, animationEffect=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 사다리생성112(self.ctx)


class 사다리생성112(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[231,232], visible=True)
        self.set_ladder(triggerIds=[131], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[132], visible=True, animationEffect=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 사다리생성121(self.ctx)


class 사다리생성121(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[241,242], visible=True)
        self.set_ladder(triggerIds=[141], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[142], visible=True, animationEffect=True)
        self.set_timer(timerId='1', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 유저감지(self.ctx)


class 사다리생성122(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[122], visible=True, animationEffect=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 사다리생성131(self.ctx)


class 사다리생성131(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[131], visible=True, animationEffect=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 사다리생성132(self.ctx)


class 사다리생성132(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[132], visible=True, animationEffect=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 사다리생성141(self.ctx)


class 사다리생성141(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[141], visible=True, animationEffect=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 사다리생성142(self.ctx)


class 사다리생성142(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[142], visible=True, animationEffect=True)
        self.set_timer(timerId='1', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 유저감지(self.ctx)


initial_state = 유저감지
