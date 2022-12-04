""" trigger/02000432_bf/error.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return None # Missing State: buff_1


initial_state = 시작
