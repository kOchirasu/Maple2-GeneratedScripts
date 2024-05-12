""" trigger/02000491_bf/portal_06.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=806, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000988], stateValue=0):
            return 포털활성화(self.ctx)


class 포털활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=806, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_interact_object(triggerIds=[10000988], state=1)
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
