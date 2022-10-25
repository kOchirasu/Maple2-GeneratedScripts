""" trigger/02010054_bf/brick_33.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[34033], visible=True, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[7033], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1133]):
            return 발판(self.ctx)


class 발판(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7033], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            self.set_mesh(triggerIds=[34033], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
