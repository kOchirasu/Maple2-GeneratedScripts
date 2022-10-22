""" trigger/02020067_bf/missiontypemonster_spawn.xml """
from common import *
import state


class 루프1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            start_combine_spawn(groupId=[528], isStart=True)
            return 루프2()


class 루프2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=150000):
            return 루프3()


class 루프3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=150000):
            return 루프2()


