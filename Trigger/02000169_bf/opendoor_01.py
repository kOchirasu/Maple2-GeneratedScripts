""" trigger/02000169_bf/opendoor_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000381], state=1)
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000381], stateValue=0):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
