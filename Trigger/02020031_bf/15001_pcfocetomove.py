""" trigger/02020031_bf/15001_pcfocetomove.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PortalOn', value=0)
        set_portal(portalId=15700, visible=False, enabled=False, minimapVisible=False) # 황금 상자 생성 구역 안쪽 포탈 / 닿아서 바깥에 있는 portal id 15701 위치로 이동 / 포탈의 target field id 수정 필요

    def on_tick(self) -> state.State:
        if user_value(key='PortalOn', value=1):
            return PortalOn()


class PortalOn(state.State):
    def on_enter(self):
        set_portal(portalId=15700, visible=False, enabled=True, minimapVisible=False) # 황금 상자 생성 구역 안쪽 포탈 / 닿아서 바깥에 있는 portal id 15701 위치로 이동 / 포탈의 target field id 수정 필요

    def on_tick(self) -> state.State:
        if user_value(key='PortalOn', value=2):
            return PortalOff()


class PortalOff(state.State):
    def on_enter(self):
        set_portal(portalId=15700, visible=False, enabled=False, minimapVisible=False) # 황금 상자 생성 구역 안쪽 포탈 / 닿아서 이동

    def on_tick(self) -> state.State:
        if user_value(key='PortalOn', value=0):
            return Wait()


