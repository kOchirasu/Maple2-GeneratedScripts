""" trigger/52000052_qd/1307_route_07roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[18071], visible=True)
        self.set_agent(triggerIds=[18072], visible=True)
        self.set_agent(triggerIds=[18073], visible=True)
        self.set_agent(triggerIds=[18074], visible=True)
        self.set_effect(triggerIds=[5007], visible=False) # 07Round_BridgeApp
        self.set_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[330700,330701,330702,330703,330704,330705,330706,330707,330708,330709,330710,330711,330712,330713,330714,330715,330716,330717,330718,330719,330720,330721], visible=False, arg3=0, delay=0, scale=0) # Real
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
        self.set_random_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=False, meshCount=22, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=False, meshCount=22, arg4=0, delay=0) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5007], visible=True) # 07Round_BridgeApp
        self.set_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[330700,330701,330702,330703,330704,330705,330706,330707,330708,330709,330710,330711,330712,330713,330714,330715,330716,330717,330718,330719,330720,330721], visible=True, meshCount=22, arg4=100, delay=50) # Real
        self.set_agent(triggerIds=[18071], visible=False)
        self.set_agent(triggerIds=[18072], visible=False)
        self.set_agent(triggerIds=[18073], visible=False)
        self.set_agent(triggerIds=[18074], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
