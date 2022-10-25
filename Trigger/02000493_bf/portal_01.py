""" trigger/02000493_bf/portal_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000978], stateValue=0):
            return 포털활성화(self.ctx)


class 포털활성화(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_interact_object(triggerIds=[10000978], state=1)
            return 대기(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
