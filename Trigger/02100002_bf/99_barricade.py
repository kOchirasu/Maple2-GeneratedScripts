""" trigger/02100002_bf/99_barricade.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PortalOn', value=0)
        set_user_value(key='MissionStart', value=0)
        set_user_value(key='DungeonClear', value=0)
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=20, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=21, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_value(key='PortalOn', value=1):
            return PortalOnDelay()


class PortalOnDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PortalOn()


class PortalOn(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=20, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=21, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_value(key='MissionStart', value=1):
            return CountDown()


class CountDown(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02100002_BF__99_BARRICADE__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return ShutDown()


#  임시 테스트용 데이터 세팅 가능 지점 포탈 열어놓기 
class ShutDown(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=20, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=21, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_value(key='DungeonClear', value=1):
            return Release()


class Release(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    pass


