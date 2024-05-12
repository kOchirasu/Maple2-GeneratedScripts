""" trigger/52000052_qd/2310_route_10roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=18, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[4018], visible=True, arg3=0, delay=0, scale=0) # PortalBarrier
        self.set_agent(triggerIds=[28101], visible=True)
        self.set_agent(triggerIds=[28102], visible=True)
        self.set_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[431000,431001,431002,431003,431004,431005,431006,431007,431008,431009,431010,431011], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=False, meshCount=12, arg4=0, delay=0)
        # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=False, meshCount=12, arg4=0, delay=0)
        # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5010], visible=True) # 10Round_BridgeApp
        self.set_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[431000,431001,431002,431003,431004,431005,431006,431007,431008,431009,431010,431011], visible=True, meshCount=12, arg4=0, delay=50) # Real
        self.set_agent(triggerIds=[28101], visible=False)
        self.set_agent(triggerIds=[28102], visible=False)
        self.set_portal(portalId=18, visible=True, enable=True, minimapVisible=False)
        self.set_mesh(triggerIds=[4018], visible=False, arg3=0, delay=0, scale=0) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
