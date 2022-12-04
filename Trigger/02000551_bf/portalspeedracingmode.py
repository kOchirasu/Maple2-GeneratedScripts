""" trigger/02000551_bf/portalspeedracingmode.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 순간이동포탈감추기(self.ctx)


class 순간이동포탈감추기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=12000, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3000, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6000, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=9000, visible=False, enable=False, minimapVisible=False) # 4계절 도로에 2개씩 배치한 순간이동 포탈
        self.set_portal(portalId=12201, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=12202, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4501, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4502, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=7801, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=7802, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=10111, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=10112, visible=False, enable=False, minimapVisible=False) # 중앙 넓은 전투판에서 12시 3시 6시 9시 넓은 전투판으로 가는 순간이동 포탈
        self.set_portal(portalId=13003, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13006, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13009, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13012, visible=False, enable=False, minimapVisible=False) # 다리도로에 1개씩 배치한 순간이동 포탈
        self.set_portal(portalId=13121, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13031, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13061, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13091, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpeedRacingMode', value=1):
            return 순간이동포탈등장(self.ctx)
        if self.user_value(key='SpeedRacingMode', value=2):
            return 종료딜레이(self.ctx)


class 순간이동포탈등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=12000, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3000, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=6000, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=9000, visible=True, enable=True, minimapVisible=True) # 4계절 도로에 2개씩 배치한 순간이동 포탈
        self.set_portal(portalId=12201, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=12202, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4501, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4502, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=7801, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=7802, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=10111, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=10112, visible=True, enable=True, minimapVisible=True) # 중앙 넓은 전투판에서 12시 3시 6시 9시 넓은 전투판으로 가는 순간이동 포탈
        self.set_portal(portalId=13003, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=13006, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=13009, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=13012, visible=True, enable=True, minimapVisible=True) # 다리도로에 1개씩 배치한 순간이동 포탈
        self.set_portal(portalId=13121, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=13031, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=13061, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=13091, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpeedRacingMode', value=0):
            return 잠시대기(self.ctx)


class 잠시대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 순간이동포탈감추기(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3800):
            return 순간이동포탈등장(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
