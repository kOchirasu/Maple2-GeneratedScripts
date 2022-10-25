""" trigger/02000176_bf_02/portal_10.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10000325], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000325], stateValue=0):
            return 생성(self.ctx)


class 생성(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=False, enable=True, minimapVisible=False)
        self.set_timer(timerId='2', seconds=2, startDelay=0, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
            return 재사용대기(self.ctx)


class 재사용대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3, startDelay=0, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 대기(self.ctx)


initial_state = 대기
