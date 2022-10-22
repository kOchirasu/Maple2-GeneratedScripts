""" trigger/63000076_cs/63000076_interact_1394.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[103], arg2=True)
        create_monster(spawnIds=[104], arg2=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001394], arg2=0):
            return 화난요정_01_1394()


class 화난요정_01_1394(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[104])
        create_monster(spawnIds=[201], arg2=True)
        create_monster(spawnIds=[202], arg2=True)
        create_monster(spawnIds=[203], arg2=True)
        create_monster(spawnIds=[204], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204]):
            return 화난요정_02_1394()


class 화난요정_02_1394(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 화난요정_03_1394()


class 화난요정_03_1394(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[103], arg2=True)
        create_monster(spawnIds=[104], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


