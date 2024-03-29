""" trigger/99999874/15001_pcfocetomove.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='PortalOn', value=0)
        self.set_portal(portalId=15700, visible=False, enable=False, minimapVisible=False) # 황금 상자 생성 구역 안쪽 포탈 / 닿아서 바깥에 있는 portal id 15701 위치로 이동 / 포탈의 target field id 수정 필요

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PortalOn', value=1):
            return PortalOn(self.ctx)


class PortalOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=15700, visible=False, enable=True, minimapVisible=False) # 황금 상자 생성 구역 안쪽 포탈 / 닿아서 바깥에 있는 portal id 15701 위치로 이동 / 포탈의 target field id 수정 필요

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PortalOn', value=2):
            return PortalOff(self.ctx)


class PortalOff(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=15700, visible=False, enable=False, minimapVisible=False) # 황금 상자 생성 구역 안쪽 포탈 / 닿아서 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PortalOn', value=0):
            return Wait(self.ctx)


initial_state = Wait
