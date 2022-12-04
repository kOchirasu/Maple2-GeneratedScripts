""" trigger/52000052_qd/1305_route_05roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[4011], visible=True, arg3=0, delay=0, scale=0) # PortalBarrier
        self.set_agent(triggerIds=[18051], visible=True)
        self.set_agent(triggerIds=[18052], visible=True)
        self.set_effect(triggerIds=[5005], visible=False) # 05Round_BridgeApp
        self.set_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[330500,330501,330502,330503,330504,330505,330506,330507,330508,330509,330510,330511,330512,330513,330514,330515,330516,330517,330518,330519], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, boxId=1):
            return StartDazzling01(self.ctx)


class StartDazzling01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5005], visible=True) # 05Round_BridgeApp
        self.set_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[330500,330501,330502,330503,330504,330505,330506,330507,330508,330509,330510,330511,330512,330513,330514,330515,330516,330517,330518,330519], visible=True, meshCount=20, arg4=100, delay=50) # Real
        self.set_agent(triggerIds=[18051], visible=False)
        self.set_agent(triggerIds=[18052], visible=False)
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=False)
        self.set_mesh(triggerIds=[4011], visible=False, arg3=0, delay=0, scale=0) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
