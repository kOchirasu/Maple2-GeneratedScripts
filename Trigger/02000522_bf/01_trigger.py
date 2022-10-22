""" trigger/02000522_bf/01_trigger.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[201]):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[301]):
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


