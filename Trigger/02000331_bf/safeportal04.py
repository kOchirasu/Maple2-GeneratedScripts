""" trigger/02000331_bf/safeportal04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=50, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[99910]):
            return 포털작동(self.ctx)


class 포털작동(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=50, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return 대기(self.ctx)


initial_state = 대기
