""" trigger/52000082_qd/main.xml """
from common import *
import state


class mapskill(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return mapskill_start()


class mapskill_start(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=70000114, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return mapskill()


