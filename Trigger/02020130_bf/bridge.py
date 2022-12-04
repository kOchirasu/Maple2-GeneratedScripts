""" trigger/02020130_bf/bridge.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032], visible=False, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=8, visible=False, enable=False, minimapVisible=False) # 1셋트 전투 끝나야 나오는 순간이동 맵 내부 포탈 최초에 감추기
        self.set_portal(portalId=9, visible=False, enable=False, minimapVisible=False) # 1셋트 전투 끝나야 나오는 순간이동 맵 내부 포탈 최초에 감추기
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False) # 1셋트 전투 끝나서 2셋트 전투판으로 이동하는 순간이동 맵 내부 포탈 최초에 감추기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[600]):
            return 작동대기상태(self.ctx)


class 작동대기상태(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BridgeAppear', value=3, operator='GreaterEqual'):
            return 다리생성(self.ctx)


class 다리생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=8, visible=True, enable=True, minimapVisible=True) # 1셋트 전투 끝나야 나오는, 8시 전투판 위에 있는 순간이동 맵 내부 포탈 최초에 감추기
        self.set_portal(portalId=9, visible=True, enable=True, minimapVisible=True) # 1셋트 전투 끝나야 나오는, 4시 전투판 위에 있는 순간이동 맵 내부 포탈 최초에 감추기
        self.set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032], visible=True, arg3=1, delay=120, scale=0.5) # BridgeSeconds, 두번째 전투판으로 이동하기 위한 다리가 순차적으로 생성
        self.set_portal(portalId=12, visible=True, enable=True, minimapVisible=True) # 1셋트 전투 끝나 2셋트 전투판으로 이동하는, 거대문의 순간이동 맵 내부 포탈 최초에 감추기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    pass


initial_state = 대기
