""" trigger/52000052_qd/1309_route_09roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=15, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[4015], visible=True, arg3=0, delay=0, scale=0) # PortalBarrier
        self.set_agent(triggerIds=[18091], visible=True)
        self.set_agent(triggerIds=[18092], visible=True)
        self.set_effect(triggerIds=[5009], visible=False) # 09Round_BridgeApp
        self.set_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[330900,330901,330902,330903,330904,330905,330906,330907,330908,330909,330910,330911], visible=False, arg3=0, delay=0, scale=0) # Real
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
        self.set_random_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=False, meshCount=12, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=False, meshCount=12, arg4=0, delay=0) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5009], visible=True) # 09Round_BridgeApp
        self.set_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[330900,330901,330902,330903,330904,330905,330906,330907,330908,330909,330910,330911], visible=True, meshCount=12, arg4=100, delay=50) # Real
        self.set_agent(triggerIds=[18091], visible=False)
        self.set_agent(triggerIds=[18092], visible=False)
        self.set_portal(portalId=15, visible=True, enable=True, minimapVisible=False)
        self.set_mesh(triggerIds=[4015], visible=False, arg3=0, delay=0, scale=0) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
