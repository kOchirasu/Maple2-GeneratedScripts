""" trigger/02020120_bf/portalstage02.xml """
import common


class Ready(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='DungeonReset', value=0) # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수
        self.set_user_value(key='Stage02', value=0) # 어느지점 포탈을 활성화 시킬지 결정하는데 사용하는 변수
        self.set_portal(portalId=2101, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2201, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2301, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3101, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3102, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3103, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3104, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3201, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3202, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3203, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3301, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3302, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3303, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3304, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3305, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3306, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4101, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4102, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4201, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4202, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4301, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4302, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5101, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5102, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5201, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5202, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5203, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5204, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5205, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5206, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5301, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5302, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5303, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5304, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5401, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6101, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6201, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6301, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6302, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6303, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6304, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return 스테이지2_시작(self.ctx)


class 스테이지2_시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Stage02', value=11):
            return 스테이지2_왼쪽진행(self.ctx)
        if self.user_value(key='Stage02', value=21):
            return 스테이지2_가운데진행(self.ctx)
        if self.user_value(key='Stage02', value=31):
            return 스테이지2_오른쪽진행(self.ctx)


class 스테이지2_왼쪽진행(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2101, visible=True, enable=True, minimapVisible=True) # 2스테이지로 가는 포탈 생성

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지2_가운데진행(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2201, visible=True, enable=True, minimapVisible=True) # 2스테이지로 가는 포탈 생성

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지2_오른쪽진행(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2301, visible=True, enable=True, minimapVisible=True) # 2스테이지로 가는 포탈 생성

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 혹시모를_던전리셋신호_대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='DungeonReset', value=1):
            return Ready(self.ctx)


initial_state = Ready
