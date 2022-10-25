""" trigger/02100002_bf/99_barricade.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PortalOn', value=0)
        self.set_user_value(key='MissionStart', value=0)
        self.set_user_value(key='DungeonClear', value=0)
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=21, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='PortalOn', value=1):
            return PortalOnDelay(self.ctx)


class PortalOnDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PortalOn(self.ctx)


class PortalOn(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=20, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=21, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MissionStart', value=1):
            return CountDown(self.ctx)


class CountDown(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02100002_BF__99_BARRICADE__0$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return ShutDown(self.ctx)


# 임시 테스트용 데이터 세팅 가능 지점 포탈 열어놓기
class ShutDown(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=21, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='DungeonClear', value=1):
            return Release(self.ctx)


class Release(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
