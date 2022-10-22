""" trigger/63000076_cs/63000076_interact_1392.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[108], arg2=False)
        create_monster(spawnIds=[115], arg2=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001392], arg2=0):
            return 화난요정_01_1392()


class 화난요정_01_1392(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[108])
        destroy_monster(spawnIds=[115])
        create_monster(spawnIds=[208], arg2=True)
        create_monster(spawnIds=[215], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[208,215]):
            return 화난요정_02_1392()


class 화난요정_02_1392(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 화난요정_03_1392()


class 화난요정_03_1392(state.State):
    def on_enter(self):
        create_monster(spawnIds=[108], arg2=False)
        create_monster(spawnIds=[115], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


