""" trigger/52000052_qd/1311_route_11roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=19, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[4019], visible=True, arg3=0, delay=0, scale=0) # PortalBarrier
        self.set_agent(triggerIds=[18111], visible=True)
        self.set_agent(triggerIds=[18112], visible=True)
        self.set_effect(triggerIds=[5011], visible=False) # 11Round_BridgeApp
        self.set_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[331100,331101,331102,331103,331104,331105,331106,331107,331108,331109], visible=False, arg3=0, delay=0, scale=0) # Real
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
        self.set_random_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=True, meshCount=3, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=False, meshCount=10, arg4=0, delay=0)
        # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=True, meshCount=3, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=False, meshCount=10, arg4=0, delay=0)
        # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5011], visible=True) # 11Round_BridgeApp
        self.set_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[331100,331101,331102,331103,331104,331105,331106,331107,331108,331109], visible=True, meshCount=10, arg4=100, delay=50) # Real
        self.set_agent(triggerIds=[18111], visible=False)
        self.set_agent(triggerIds=[18112], visible=False)
        self.set_portal(portalId=19, visible=True, enable=True, minimapVisible=False)
        self.set_mesh(triggerIds=[4019], visible=False, arg3=0, delay=0, scale=0) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
