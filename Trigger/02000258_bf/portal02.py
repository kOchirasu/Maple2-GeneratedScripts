""" trigger/02000258_bf/portal02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=52, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10000663], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000663], stateValue=0):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=52, visible=False, enable=True, minimapVisible=False)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.set_portal(portalId=52, visible=False, enable=False, minimapVisible=False)
            return 재사용대기(self.ctx)


class 재사용대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 대기(self.ctx)


initial_state = 대기
