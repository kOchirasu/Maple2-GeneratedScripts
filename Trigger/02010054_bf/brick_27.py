""" trigger/02010054_bf/brick_27.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[34027], visible=True, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[7027], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1127]):
            return 발판(self.ctx)


class 발판(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7027], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            self.set_mesh(triggerIds=[34027], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
