""" trigger/02000432_bf/error.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return None # Missing State: buff_1


initial_state = 시작
