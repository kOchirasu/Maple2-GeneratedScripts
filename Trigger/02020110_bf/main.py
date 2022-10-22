""" trigger/02020110_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=7, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901], jobCode=0):
            return 시작()


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[902]):
            return 번방1()


class 번방1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,120], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,120]):
            set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            return 번방2()


class 번방2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102,103,104,105,106,107], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102,103,104,105,106,107]):
            set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)
            return 번방3()


class 번방3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[108,109,110,111,112,113], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[108,109,110,111,112,113]):
            set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True)
            return 번방4()


class 번방4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[114,115,116,117,118,119], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[114,115,116,117,118,119]):
            return 다음블록이동()


class 다음블록이동(state.State):
    def on_enter(self):
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True)


