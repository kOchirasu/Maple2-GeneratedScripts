""" trigger/02020130_bf/bridge.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032], visible=False, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=8, visible=False, enabled=False, minimapVisible=False) # 1셋트 전투 끝나야 나오는 순간이동 맵 내부 포탈 최초에 감추기
        set_portal(portalId=9, visible=False, enabled=False, minimapVisible=False) # 1셋트 전투 끝나야 나오는 순간이동 맵 내부 포탈 최초에 감추기
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False) # 1셋트 전투 끝나서 2셋트 전투판으로 이동하는 순간이동 맵 내부 포탈 최초에 감추기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[600]):
            return 작동대기상태()


class 작동대기상태(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BridgeAppear', value=3, operator='GreaterEqual'):
            return 다리생성()


class 다리생성(state.State):
    def on_enter(self):
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True) # 1셋트 전투 끝나야 나오는, 8시 전투판 위에 있는 순간이동 맵 내부 포탈 최초에 감추기
        set_portal(portalId=9, visible=True, enabled=True, minimapVisible=True) # 1셋트 전투 끝나야 나오는, 4시 전투판 위에 있는 순간이동 맵 내부 포탈 최초에 감추기
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032], visible=True, arg3=1, arg4=120, arg5=0.5) # BridgeSeconds, 두번째 전투판으로 이동하기 위한 다리가 순차적으로 생성
        set_portal(portalId=12, visible=True, enabled=True, minimapVisible=True) # 1셋트 전투 끝나 2셋트 전투판으로 이동하는, 거대문의 순간이동 맵 내부 포탈 최초에 감추기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


class 연출종료(state.State):
    pass


