""" trigger/02020120_bf/portalstage03.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_user_value(key='DungeonReset', value=0) # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수
        set_user_value(key='Stage03', value=0) # 어느지점 포탈을 활성화 시킬지 결정하는데 사용하는 변수

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 스테이지3_시작()


class 스테이지3_시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Stage03', value=11):
            return 스테이지3_왼쪽_왼쪽진행()
        if user_value(key='Stage03', value=12):
            return 스테이지3_왼쪽_가운데진행()
        if user_value(key='Stage03', value=21):
            return 스테이지3_가운데_왼쪽진행()
        if user_value(key='Stage03', value=22):
            return 스테이지3_가운데_가운데진행()
        if user_value(key='Stage03', value=23):
            return 스테이지3_가운데_오른쪽진행()
        if user_value(key='Stage03', value=31):
            return 스테이지3_오른쪽_가운데진행()
        if user_value(key='Stage03', value=32):
            return 스테이지3_오른쪽_오른쪽진행()


class 스테이지3_왼쪽_왼쪽진행(state.State):
    def on_enter(self):
        set_portal(portalId=3101, visible=True, enabled=True, minimapVisible=True) # 3스테이지로 가는 포탈 생성
        set_portal(portalId=3102, visible=True, enabled=True, minimapVisible=True) # 3스테이지로 가는 포탈 생성

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지3_왼쪽_가운데진행(state.State):
    def on_enter(self):
        set_portal(portalId=3103, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3104, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지3_가운데_왼쪽진행(state.State):
    def on_enter(self):
        set_portal(portalId=3201, visible=True, enabled=True, minimapVisible=True) # 3스테이지로 가는 포탈 생성

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지3_가운데_가운데진행(state.State):
    def on_enter(self):
        set_portal(portalId=3202, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지3_가운데_오른쪽진행(state.State):
    def on_enter(self):
        set_portal(portalId=3203, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지3_오른쪽_가운데진행(state.State):
    def on_enter(self):
        set_portal(portalId=3301, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3302, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3303, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지3_오른쪽_오른쪽진행(state.State):
    def on_enter(self):
        set_portal(portalId=3304, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3305, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3306, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 혹시모를_던전리셋신호_대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='DungeonReset', value=1):
            return Ready()


