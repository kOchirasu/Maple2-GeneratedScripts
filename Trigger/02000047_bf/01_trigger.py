""" trigger/02000047_bf/01_trigger.xml """
import common


class 반응대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000084], state=1)
        self.set_interact_object(triggerIds=[10000085], state=1)
        self.set_mesh(triggerIds=[10,11,12,13,14,15,16,17], visible=False) # 다리안보임

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000084,10000085], stateValue=0):
            return 다리생성1011(self.ctx)


class 다리생성1011(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[10,11], visible=True) # 다리보임
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 다리생성1213(self.ctx)


class 다리생성1213(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[12,13], visible=True) # 다리보임
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 다리생성1415(self.ctx)


class 다리생성1415(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[14,15], visible=True) # 다리보임
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 다리생성1617(self.ctx)


class 다리생성1617(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[16,17], visible=True) # 다리보임
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 다리제거(self.ctx)


class 다리제거(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='99', seconds=6)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='99'):
            self.set_mesh(triggerIds=[10,11,12,13,14,15,16,17], visible=False)
            return 트리거초기화2(self.ctx)


class 트리거초기화2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 반응대기(self.ctx)


initial_state = 반응대기
