""" trigger/02000531_bf/statue12.xml """
import trigger_api


class 세팅(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[12], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 수신대기(self.ctx)


class 수신대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StatueAnimal01Death', value=1):
            self.set_mesh(triggerIds=[12], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[12], visible=False, arg3=0, delay=0, scale=0)


initial_state = 세팅
