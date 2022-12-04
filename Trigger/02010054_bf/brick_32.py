""" trigger/02010054_bf/brick_32.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[34032], visible=True, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[7032], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1132]):
            return 발판(self.ctx)


class 발판(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7032], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            self.set_mesh(triggerIds=[34032], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
