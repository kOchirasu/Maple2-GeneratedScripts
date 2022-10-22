""" trigger/02020142_bf/setportal.xml """
from common import *
import state


class 전투체크(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 대기99()


class 대기99(state.State):
    pass


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=118, visible=False, enabled=False, minimapVisible=False) # 1스테이지에서 맨 왼쪽 지점으로 진행하는 포탈
        set_portal(portalId=128, visible=False, enabled=False, minimapVisible=False) # 1스테이지에서 가운데 지점으로 진행하는 포탈
        set_portal(portalId=138, visible=False, enabled=False, minimapVisible=False) # 1스테이지에서 맨 오른쪽 지점으로 진행하는 포탈
        set_portal(portalId=218, visible=False, enabled=False, minimapVisible=False) # 맨 왼쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        set_portal(portalId=228, visible=False, enabled=False, minimapVisible=False) # 가운데 지점 2스테이지에서 다음 단계 넘어가는 포탈
        set_portal(portalId=238, visible=False, enabled=False, minimapVisible=False) # 맨 오른쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        set_portal(portalId=318, visible=False, enabled=False, minimapVisible=False) # 맨 왼쪽 지점에서 보스 전투판으로 넘어가는 포탈
        set_portal(portalId=328, visible=False, enabled=False, minimapVisible=False) # 가운데 지점에서 마지막 스테이지로 넘어가는 포탈
        set_portal(portalId=338, visible=False, enabled=False, minimapVisible=False) # 맨 오른쪽 지점에서 보스 전투판으로 넘어가는 포탈
        set_portal(portalId=428, visible=False, enabled=False, minimapVisible=False) # 가운데 지점 마지막 스테이지에서 보스 전투판으로 넘어가는 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return 포탈생성()
        if user_value(key='SetLight', value=1):
            return 포탈생성()


class 포탈생성(state.State):
    def on_enter(self):
        set_portal(portalId=118, visible=True, enabled=True, minimapVisible=True) # 1스테이지에서 맨 왼쪽 지점으로 진행하는 포탈
        set_portal(portalId=128, visible=True, enabled=True, minimapVisible=True) # 1스테이지에서 가운데 지점으로 진행하는 포탈
        set_portal(portalId=138, visible=True, enabled=True, minimapVisible=True) # 1스테이지에서 맨 오른쪽 지점으로 진행하는 포탈
        set_portal(portalId=218, visible=True, enabled=True, minimapVisible=True) # 맨 왼쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        set_portal(portalId=228, visible=True, enabled=True, minimapVisible=True) # 가운데 지점 2스테이지에서 다음 단계 넘어가는 포탈
        set_portal(portalId=238, visible=True, enabled=True, minimapVisible=True) # 맨 오른쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        set_portal(portalId=318, visible=True, enabled=True, minimapVisible=True) # 맨 왼쪽 지점에서 보스 전투판으로 넘어가는 포탈
        set_portal(portalId=328, visible=True, enabled=True, minimapVisible=True) # 가운데 지점에서 마지막 스테이지로 넘어가는 포탈
        set_portal(portalId=338, visible=True, enabled=True, minimapVisible=True) # 맨 오른쪽 지점에서 보스 전투판으로 넘어가는 포탈
        set_portal(portalId=428, visible=True, enabled=True, minimapVisible=True) # 가운데 지점 마지막 스테이지에서 보스 전투판으로 넘어가는 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


