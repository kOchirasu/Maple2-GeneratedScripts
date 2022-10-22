""" trigger/63000076_cs/63000076_interact_1395.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[116], arg2=False)
        create_monster(spawnIds=[117], arg2=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001395], arg2=0):
            return 화난요정_01_1395()


class 화난요정_01_1395(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[116])
        destroy_monster(spawnIds=[117])
        create_monster(spawnIds=[216], arg2=True)
        create_monster(spawnIds=[217], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[216,217]):
            return 화난요정_02_1395()


class 화난요정_02_1395(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 화난요정_03_1395()


class 화난요정_03_1395(state.State):
    def on_enter(self):
        create_monster(spawnIds=[116], arg2=False)
        create_monster(spawnIds=[117], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


