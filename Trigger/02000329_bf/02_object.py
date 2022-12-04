""" trigger/02000329_bf/02_object.xml """
import trigger_api


class 오브젝트_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[10001], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            return 오브젝트_01_작동(self.ctx)


class 오브젝트_01_작동(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[10001], enable=True)


initial_state = 오브젝트_01
