""" trigger/02000427_bf/portal4578.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False) # 4시방향 태엽폭탄 있는 곳의 순간이동 포탈 초기화 하기, 최초에는 모습을 안보임
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False) # 4시방향 태엽폭탄 있는 곳의 순간이동 포탈 초기화 하기, 최초에는 모습을 안보임
        set_portal(portalId=7, visible=False, enabled=False, minimapVisible=False) # 7시방향 태엽폭탄 있는 곳의 순간이동 포탈 초기화 하기, 최초에는 모습을 안보임
        set_portal(portalId=8, visible=False, enabled=False, minimapVisible=False) # 8시방향 태엽폭탄 있는 곳의 순간이동 포탈 초기화 하기, 최초에는 모습을 안보임

    def on_tick(self) -> state.State:
        if user_value(key='ThirdPhase', value=1):
            return 순간이동포탈생성()


class 순간이동포탈생성(state.State):
    def on_enter(self):
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True) # 4시방향 태엽폭탄 있는 곳에 순간이동 포탈 등장시킴
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True) # 4시방향 태엽폭탄 있는 곳에 순간이동 포탈 등장시킴
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True) # 7시방향 태엽폭탄 있는 곳에 순간이동 포탈 등장시킴
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True) # 8시방향 태엽폭탄 있는 곳에 순간이동 포탈 등장시킴


class 종료(state.State):
    pass


