""" trigger/02000331_bf/safeportal05.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=52, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[99994]):
            return 포털작동(self.ctx)


class 포털작동(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=52, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return 대기(self.ctx)


initial_state = 대기
