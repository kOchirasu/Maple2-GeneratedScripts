""" trigger/02010050_bf/bossspawn01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[99], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 보스처치()


class 보스처치(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[99])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


