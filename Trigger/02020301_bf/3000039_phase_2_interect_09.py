""" trigger/02020301_bf/3000039_phase_2_interect_09.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return None # Missing State: 시작


