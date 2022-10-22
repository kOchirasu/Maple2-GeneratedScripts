""" trigger/63000076_cs/63000076_interact_1393.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[109], arg2=True)
        create_monster(spawnIds=[110], arg2=True)
        create_monster(spawnIds=[111], arg2=True)
        create_monster(spawnIds=[112], arg2=True)
        create_monster(spawnIds=[113], arg2=True)
        create_monster(spawnIds=[114], arg2=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001393], arg2=0):
            return 화난요정_01_1393()


class 화난요정_01_1393(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[109])
        destroy_monster(spawnIds=[110])
        destroy_monster(spawnIds=[111])
        destroy_monster(spawnIds=[112])
        destroy_monster(spawnIds=[113])
        destroy_monster(spawnIds=[114])
        create_monster(spawnIds=[209], arg2=True)
        create_monster(spawnIds=[210], arg2=True)
        create_monster(spawnIds=[211], arg2=True)
        create_monster(spawnIds=[212], arg2=True)
        create_monster(spawnIds=[213], arg2=True)
        create_monster(spawnIds=[214], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[209,210,211,212,213,214]):
            return 화난요정_02_1393()


class 화난요정_02_1393(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 화난요정_03_1393()


class 화난요정_03_1393(state.State):
    def on_enter(self):
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[110], arg2=False)
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[112], arg2=False)
        create_monster(spawnIds=[113], arg2=False)
        create_monster(spawnIds=[114], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


