""" trigger/02000523_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10]):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)
        create_monster(spawnIds=[900])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900]):
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
        set_portal(portalId=12, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13, visible=True, enabled=True, minimapVisible=True)


