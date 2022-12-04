""" trigger/02000378_bf/2301_route_01roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[28011], visible=True)
        self.set_agent(triggerIds=[28012], visible=True)
        self.set_agent(triggerIds=[28013], visible=True)
        self.set_agent(triggerIds=[28014], visible=True)
        self.set_mesh(triggerIds=[230100,230101,230102,230103,230104,230105,230106,230107,230108,230109,230110,230111,230112,230113,230114,230115,230116,230117,230118,230119,230120,230121,230122,230123], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[430100,430101,430102,430103,430104,430105,430106,430107,430108,430109,430110,430111,430112,430113,430114,430115,430116,430117,430118,430119,430120,430121,430122,430123], visible=False, arg3=0, delay=0, scale=0) # Real

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
        self.set_random_mesh(triggerIds=[230100,230101,230102,230103,230104,230105,230106,230107,230108,230109,230110,230111,230112,230113,230114,230115,230116,230117,230118,230119,230120,230121,230122,230123], visible=True, meshCount=8, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[230100,230101,230102,230103,230104,230105,230106,230107,230108,230109,230110,230111,230112,230113,230114,230115,230116,230117,230118,230119,230120,230121,230122,230123], visible=False, meshCount=24, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[230100,230101,230102,230103,230104,230105,230106,230107,230108,230109,230110,230111,230112,230113,230114,230115,230116,230117,230118,230119,230120,230121,230122,230123], visible=True, meshCount=8, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[230100,230101,230102,230103,230104,230105,230106,230107,230108,230109,230110,230111,230112,230113,230114,230115,230116,230117,230118,230119,230120,230121,230122,230123], visible=False, meshCount=24, arg4=0, delay=0) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True) # 01Round_BridgeApp
        self.set_mesh(triggerIds=[230100,230101,230102,230103,230104,230105,230106,230107,230108,230109,230110,230111,230112,230113,230114,230115,230116,230117,230118,230119,230120,230121,230122,230123], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[430100,430101,430102,430103,430104,430105,430106,430107,430108,430109,430110,430111,430112,430113,430114,430115,430116,430117,430118,430119,430120,430121,430122,430123], visible=True, meshCount=24, arg4=100, delay=50) # Real
        self.set_agent(triggerIds=[28011], visible=False)
        self.set_agent(triggerIds=[28012], visible=False)
        self.set_agent(triggerIds=[28013], visible=False)
        self.set_agent(triggerIds=[28014], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[230100,230101,230102,230103,230104,230105,230106,230107,230108,230109,230110,230111,230112,230113,230114,230115,230116,230117,230118,230119,230120,230121,230122,230123], visible=False, arg3=500, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
