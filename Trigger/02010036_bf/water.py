""" trigger/02010036_bf/water.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=30, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 부서짐(self.ctx)


class 부서짐(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=30, scale=2)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[101]):
            return 대기(self.ctx)


initial_state = 대기
