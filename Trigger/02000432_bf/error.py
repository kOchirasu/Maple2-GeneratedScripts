""" trigger/02000432_bf/error.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return None # Missing State: buff_1


