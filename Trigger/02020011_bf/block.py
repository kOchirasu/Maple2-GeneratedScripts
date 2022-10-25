""" trigger/02020011_bf/block.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001], visible=True, scale=5)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 딜레이(self.ctx)


class 딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 사라짐(self.ctx)


class 사라짐(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001], visible=False, scale=5)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[101]):
            return 딜레이2(self.ctx)


class 딜레이2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 대기(self.ctx)


initial_state = 대기
