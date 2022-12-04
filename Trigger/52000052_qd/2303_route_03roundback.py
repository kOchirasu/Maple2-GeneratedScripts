""" trigger/52000052_qd/2303_route_03roundback.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[28031], visible=True)
        self.set_agent(triggerIds=[28032], visible=True)
        self.set_agent(triggerIds=[28033], visible=True)
        self.set_agent(triggerIds=[28034], visible=True)
        self.set_mesh(triggerIds=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[430300,430301,430302,430303,430304,430305,430306,430307,430308,430309,430310,430311,430312,430313,430314,430315,430316,430317,430318,430319], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=True) # 03Round_BridgeApp
        self.set_mesh(triggerIds=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[430300,430301,430302,430303,430304,430305,430306,430307,430308,430309,430310,430311,430312,430313,430314,430315,430316,430317,430318,430319], visible=True, meshCount=20, arg4=100, delay=50) # Real
        self.set_agent(triggerIds=[28031], visible=False)
        self.set_agent(triggerIds=[28032], visible=False)
        self.set_agent(triggerIds=[28033], visible=False)
        self.set_agent(triggerIds=[28034], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[230300,230301,230302,230303,230304,230305,230306,230307,230308,230309,230310,230311,230312,230313,230314,230315,230316,230317,230318,230319], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
