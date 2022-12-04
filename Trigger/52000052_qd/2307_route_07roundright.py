""" trigger/52000052_qd/2307_route_07roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[28071], visible=True)
        self.set_agent(triggerIds=[28072], visible=True)
        self.set_agent(triggerIds=[28073], visible=True)
        self.set_agent(triggerIds=[28074], visible=True)
        self.set_mesh(triggerIds=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[430700,430701,430702,430703,430704,430705,430706,430707,430708,430709,430710,430711,430712,430713,430714,430715,430716,430717,430718,430719], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5007], visible=True) # 07Round_BridgeApp
        self.set_mesh(triggerIds=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[430700,430701,430702,430703,430704,430705,430706,430707,430708,430709,430710,430711,430712,430713,430714,430715,430716,430717,430718,430719], visible=True, meshCount=20, arg4=0, delay=50) # Real
        self.set_agent(triggerIds=[28071], visible=False)
        self.set_agent(triggerIds=[28072], visible=False)
        self.set_agent(triggerIds=[28073], visible=False)
        self.set_agent(triggerIds=[28074], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[230700,230701,230702,230703,230704,230705,230706,230707,230708,230709,230710,230711,230712,230713,230714,230715,230716,230717,230718,230719], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
