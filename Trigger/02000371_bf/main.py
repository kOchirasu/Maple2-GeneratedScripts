""" trigger/02000371_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 카오스레이드()


class 카오스레이드(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2101], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2101]):
            return 초대기2()


class 초대기2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 던전클리어()


class 던전클리어(state.State):
    def on_enter(self):
        dungeon_clear()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 포털개방()


class 포털개방(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


