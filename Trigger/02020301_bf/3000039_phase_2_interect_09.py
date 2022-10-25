""" trigger/02020301_bf/3000039_phase_2_interect_09.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return None # Missing State: 시작


initial_state = 대기
