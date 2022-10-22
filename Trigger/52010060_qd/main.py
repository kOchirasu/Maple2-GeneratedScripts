""" trigger/52010060_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001], jobCode=0):
            return 크림슨발록등장()


class 크림슨발록등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=True) # 크림슨 발록

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


