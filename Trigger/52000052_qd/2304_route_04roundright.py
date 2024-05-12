""" trigger/52000052_qd/2304_route_04roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[28041], visible=True)
        self.set_agent(triggerIds=[28042], visible=True)
        self.set_agent(triggerIds=[28043], visible=True)
        self.set_agent(triggerIds=[28044], visible=True)
        self.set_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[430400,430401,430402,430403,430404,430405,430406,430407,430408,430409,430410,430411,430412,430413,430414,430415,430416,430417,430418,430419], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=False, meshCount=20, arg4=0, delay=0)
        # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=False, meshCount=20, arg4=0, delay=0)
        # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5004], visible=True) # 04Round_BridgeApp
        self.set_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[430400,430401,430402,430403,430404,430405,430406,430407,430408,430409,430410,430411,430412,430413,430414,430415,430416,430417,430418,430419], visible=True, meshCount=20, arg4=0, delay=50) # Real
        self.set_agent(triggerIds=[28041], visible=False)
        self.set_agent(triggerIds=[28042], visible=False)
        self.set_agent(triggerIds=[28043], visible=False)
        self.set_agent(triggerIds=[28044], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
