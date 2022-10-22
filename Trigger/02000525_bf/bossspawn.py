""" trigger/02000525_bf/bossspawn.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10]):
            return 난이도별보스등장()


class 난이도별보스등장(state.State):
    def on_tick(self) -> state.State:
        if dungeon_id(dungeonId=23048003):
            return 일반난이도_보스등장()
        if dungeon_id(dungeonId=23049003):
            return 어려움난이도_보스등장()
        if wait_tick(waitTick=1100):
            return 일반난이도_보스등장()


class 일반난이도_보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 클리어처리()


class 어려움난이도_보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102]):
            return 클리어처리()


class 클리어처리(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            dungeon_clear()
            return 종료처리()


class 종료처리(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)


