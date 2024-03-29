""" trigger/02000042_bf/portal_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000583], state=1)
        self.set_portal(portalId=6, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000583], stateValue=0):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=5)
        self.set_portal(portalId=6, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 대기(self.ctx)


initial_state = 대기
