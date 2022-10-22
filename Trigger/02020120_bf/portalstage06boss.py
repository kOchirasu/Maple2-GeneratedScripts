""" trigger/02020120_bf/portalstage06boss.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_user_value(key='DungeonReset', value=0) # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수
        set_user_value(key='Stage06', value=0) # 어느지점 포탈을 활성화 시킬지 결정하는데 사용하는 변수

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 스테이지6_시작()


class 스테이지6_시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Stage06', value=11):
            return 스테이지6_왼쪽_가운데진행()
        if user_value(key='Stage06', value=21):
            return 스테이지6_가운데_가운데진행()
        if user_value(key='Stage06', value=31):
            return 스테이지6_오른쪽_가운데진행()


class 스테이지6_왼쪽_가운데진행(state.State):
    def on_enter(self):
        set_portal(portalId=6101, visible=True, enabled=True, minimapVisible=True) # 6스테이지 보스로 가는 포탈 생성

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지6_가운데_가운데진행(state.State):
    def on_enter(self):
        set_portal(portalId=6201, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지6_오른쪽_가운데진행(state.State):
    def on_enter(self):
        set_portal(portalId=6301, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=6302, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=6303, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=6304, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 혹시모를_던전리셋신호_대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='DungeonReset', value=1):
            return Ready()


