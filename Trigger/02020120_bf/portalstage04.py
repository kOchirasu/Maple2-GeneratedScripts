""" trigger/02020120_bf/portalstage04.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_user_value(key='DungeonReset', value=0) # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수
        set_user_value(key='Stage04', value=0) # 어느지점 포탈을 활성화 시킬지 결정하는데 사용하는 변수

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 스테이지4_시작()


class 스테이지4_시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Stage04', value=11):
            return 스테이지4_왼쪽_왼쪽진행()
        if user_value(key='Stage04', value=12):
            return 스테이지4_왼쪽_왼쪽가운데진행()
        if user_value(key='Stage04', value=21):
            return 스테이지4_가운데_왼쪽가운데진행()
        if user_value(key='Stage04', value=22):
            return 스테이지4_가운데_오른쪽가운데진행()
        if user_value(key='Stage04', value=31):
            return 스테이지4_오른쪽_오른쪽가운데진행()
        if user_value(key='Stage04', value=32):
            return 스테이지4_오른쪽_오른쪽진행()


class 스테이지4_왼쪽_왼쪽진행(state.State):
    def on_enter(self):
        set_portal(portalId=4101, visible=True, enabled=True, minimapVisible=True) # 4스테이지로 가는 포탈 생성

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지4_왼쪽_왼쪽가운데진행(state.State):
    def on_enter(self):
        set_portal(portalId=4102, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지4_가운데_왼쪽가운데진행(state.State):
    def on_enter(self):
        set_portal(portalId=4201, visible=True, enabled=True, minimapVisible=True) # 4스테이지로 가는 포탈 생성

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지4_가운데_오른쪽가운데진행(state.State):
    def on_enter(self):
        set_portal(portalId=4202, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지4_오른쪽_오른쪽가운데진행(state.State):
    def on_enter(self):
        set_portal(portalId=4301, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 스테이지4_오른쪽_오른쪽진행(state.State):
    def on_enter(self):
        set_portal(portalId=4302, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기()


class 혹시모를_던전리셋신호_대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='DungeonReset', value=1):
            return Ready()


