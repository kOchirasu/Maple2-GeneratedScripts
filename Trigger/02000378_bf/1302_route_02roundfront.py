""" trigger/02000378_bf/1302_route_02roundfront.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[18021], visible=True)
        self.set_agent(triggerIds=[18022], visible=True)
        self.set_agent(triggerIds=[18023], visible=True)
        self.set_agent(triggerIds=[18024], visible=True)
        self.set_effect(triggerIds=[5002], visible=False) # 02Round_BridgeApp
        self.set_mesh(triggerIds=[130200,130201,130202,130203,130204,130205,130206,130207,130208,130209,130210,130211,130212,130213,130214,130215,130216,130217,130218,130219,130220,130221], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[330200,330201,330202,330203,330204,330205,330206,330207,330208,330209,330210,330211,330212,330213,330214,330215,330216,330217,330218,330219,330220,330221], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[130200,130201,130202,130203,130204,130205,130206,130207,130208,130209,130210,130211,130212,130213,130214,130215,130216,130217,130218,130219,130220,130221], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[130200,130201,130202,130203,130204,130205,130206,130207,130208,130209,130210,130211,130212,130213,130214,130215,130216,130217,130218,130219,130220,130221], visible=False, meshCount=22, arg4=0, delay=0)
        # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[130200,130201,130202,130203,130204,130205,130206,130207,130208,130209,130210,130211,130212,130213,130214,130215,130216,130217,130218,130219,130220,130221], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[130200,130201,130202,130203,130204,130205,130206,130207,130208,130209,130210,130211,130212,130213,130214,130215,130216,130217,130218,130219,130220,130221], visible=False, meshCount=22, arg4=0, delay=0)
        # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5002], visible=True) # 02Round_BridgeApp
        self.set_mesh(triggerIds=[130200,130201,130202,130203,130204,130205,130206,130207,130208,130209,130210,130211,130212,130213,130214,130215,130216,130217,130218,130219,130220,130221], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[330200,330201,330202,330203,330204,330205,330206,330207,330208,330209,330210,330211,330212,330213,330214,330215,330216,330217,330218,330219,330220,330221], visible=True, meshCount=22, arg4=100, delay=50) # Real
        self.set_agent(triggerIds=[18021], visible=False)
        self.set_agent(triggerIds=[18022], visible=False)
        self.set_agent(triggerIds=[18023], visible=False)
        self.set_agent(triggerIds=[18024], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[130200,130201,130202,130203,130204,130205,130206,130207,130208,130209,130210,130211,130212,130213,130214,130215,130216,130217,130218,130219,130220,130221], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
