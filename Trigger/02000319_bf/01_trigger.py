""" trigger/02000319_bf/01_trigger.xml """
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
            return 포털()


class 포털(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            dungeon_clear()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)


