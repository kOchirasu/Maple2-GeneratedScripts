""" trigger/52000052_qd/1310_route_10roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=17, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[4017], visible=True, arg3=0, delay=0, scale=0) # PortalBarrier
        self.set_agent(triggerIds=[18101], visible=True)
        self.set_agent(triggerIds=[18102], visible=True)
        self.set_effect(triggerIds=[5010], visible=False) # 10Round_BridgeApp
        self.set_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[331000,331001,331002,331003,331004,331005,331006,331007,331008,331009,331010,331011], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, minUsers='1'):
            return StartDazzling01(self.ctx)


class StartDazzling01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=False, meshCount=12, arg4=0, delay=0)
        # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=False, meshCount=12, arg4=0, delay=0)
        # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5010], visible=True) # 10Round_BridgeApp
        self.set_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[331000,331001,331002,331003,331004,331005,331006,331007,331008,331009,331010,331011], visible=True, meshCount=12, arg4=100, delay=50) # Real
        self.set_agent(triggerIds=[18101], visible=False)
        self.set_agent(triggerIds=[18102], visible=False)
        self.set_portal(portalId=17, visible=True, enable=True, minimapVisible=False)
        self.set_mesh(triggerIds=[4017], visible=False, arg3=0, delay=0, scale=0) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
