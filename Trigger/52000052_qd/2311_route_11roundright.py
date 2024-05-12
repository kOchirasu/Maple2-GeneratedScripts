""" trigger/52000052_qd/2311_route_11roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[4010], visible=True, arg3=0, delay=0, scale=0) # PortalBarrier
        self.set_agent(triggerIds=[28111], visible=True)
        self.set_agent(triggerIds=[28112], visible=True)
        self.set_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[431100,431101,431102,431103,431104,431105,431106,431107,431108,431109,431110,431111], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=False, meshCount=12, arg4=0, delay=0)
        # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=False, meshCount=12, arg4=0, delay=0)
        # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5011], visible=True) # 11Round_BridgeApp
        self.set_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[431100,431101,431102,431103,431104,431105,431106,431107,431108,431109,431110,431111], visible=True, meshCount=12, arg4=0, delay=50) # Real
        self.set_agent(triggerIds=[28111], visible=False)
        self.set_agent(triggerIds=[28112], visible=False)
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=False)
        self.set_mesh(triggerIds=[4010], visible=False, arg3=0, delay=0, scale=0) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
