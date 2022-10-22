""" trigger/02000551_bf/portalspeedracingmode.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 순간이동포탈감추기()


class 순간이동포탈감추기(state.State):
    def on_enter(self):
        set_portal(portalId=12000, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=3000, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=6000, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=9000, visible=False, enabled=False, minimapVisible=False) # 4계절 도로에 2개씩 배치한 순간이동 포탈
        set_portal(portalId=12201, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=12202, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=4501, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=4502, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=7801, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=7802, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=10111, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=10112, visible=False, enabled=False, minimapVisible=False) # 중앙 넓은 전투판에서 12시 3시 6시 9시 넓은 전투판으로 가는 순간이동 포탈
        set_portal(portalId=13003, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13006, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13009, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13012, visible=False, enabled=False, minimapVisible=False) # 다리도로에 1개씩 배치한 순간이동 포탈
        set_portal(portalId=13121, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13031, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13061, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13091, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_value(key='SpeedRacingMode', value=1):
            return 순간이동포탈등장()
        if user_value(key='SpeedRacingMode', value=2):
            return 종료딜레이()


class 순간이동포탈등장(state.State):
    def on_enter(self):
        set_portal(portalId=12000, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3000, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=6000, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=9000, visible=True, enabled=True, minimapVisible=True) # 4계절 도로에 2개씩 배치한 순간이동 포탈
        set_portal(portalId=12201, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=12202, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=4501, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=4502, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=7801, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=7802, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=10111, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=10112, visible=True, enabled=True, minimapVisible=True) # 중앙 넓은 전투판에서 12시 3시 6시 9시 넓은 전투판으로 가는 순간이동 포탈
        set_portal(portalId=13003, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13006, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13009, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13012, visible=True, enabled=True, minimapVisible=True) # 다리도로에 1개씩 배치한 순간이동 포탈
        set_portal(portalId=13121, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13031, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13061, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13091, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_value(key='SpeedRacingMode', value=0):
            return 잠시대기()


class 잠시대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 순간이동포탈감추기()


class 종료딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3800):
            return 순간이동포탈등장()


class 종료(state.State):
    pass


