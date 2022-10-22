""" trigger/80000013_bonus/main.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return start()


class start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[108], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=60000):
            return end()


class end(state.State):
    pass


