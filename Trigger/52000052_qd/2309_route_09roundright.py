""" trigger/52000052_qd/2309_route_09roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=16, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[4016], visible=True, arg3=0, delay=0, scale=0) # PortalBarrier
        self.set_agent(triggerIds=[28091], visible=True)
        self.set_agent(triggerIds=[28092], visible=True)
        self.set_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[430900,430901,430902,430903,430904,430905,430906,430907,430908,430909], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=True, meshCount=3, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, meshCount=10, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=True, meshCount=3, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, meshCount=10, arg4=0, delay=0) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5009], visible=True) # 09Round_BridgeApp
        self.set_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[430900,430901,430902,430903,430904,430905,430906,430907,430908,430909], visible=True, meshCount=10, arg4=0, delay=50) # Real
        self.set_agent(triggerIds=[28091], visible=False)
        self.set_agent(triggerIds=[28092], visible=False)
        self.set_portal(portalId=16, visible=True, enable=True, minimapVisible=False)
        self.set_mesh(triggerIds=[4016], visible=False, arg3=0, delay=0, scale=0) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
