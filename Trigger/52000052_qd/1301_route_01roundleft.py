""" trigger/52000052_qd/1301_route_01roundleft.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[18011], visible=True)
        self.set_agent(triggerIds=[18012], visible=True)
        self.set_agent(triggerIds=[18013], visible=True)
        self.set_agent(triggerIds=[18014], visible=True)
        self.set_effect(triggerIds=[5001], visible=False) # 01Round_BridgeApp
        self.set_mesh(triggerIds=[130100,130101,130102,130103,130104,130105,130106,130107,130108,130109,130110,130111,130112,130113,130114,130115,130116,130117,130118,130119,130120,130121,130122,130123], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[330100,330101,330102,330103,330104,330105,330106,330107,330108,330109,330110,330111,330112,330113,330114,330115,330116,330117,330118,330119,330120,330121,330122,330123], visible=False, arg3=0, delay=0, scale=0) # Real
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
        self.set_random_mesh(triggerIds=[130100,130101,130102,130103,130104,130105,130106,130107,130108,130109,130110,130111,130112,130113,130114,130115,130116,130117,130118,130119,130120,130121,130122,130123], visible=True, meshCount=8, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[130100,130101,130102,130103,130104,130105,130106,130107,130108,130109,130110,130111,130112,130113,130114,130115,130116,130117,130118,130119,130120,130121,130122,130123], visible=False, meshCount=24, arg4=0, delay=0)
        # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[130100,130101,130102,130103,130104,130105,130106,130107,130108,130109,130110,130111,130112,130113,130114,130115,130116,130117,130118,130119,130120,130121,130122,130123], visible=True, meshCount=8, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[130100,130101,130102,130103,130104,130105,130106,130107,130108,130109,130110,130111,130112,130113,130114,130115,130116,130117,130118,130119,130120,130121,130122,130123], visible=False, meshCount=24, arg4=0, delay=0)
        # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=True) # 01Round_BridgeApp
        self.set_mesh(triggerIds=[130100,130101,130102,130103,130104,130105,130106,130107,130108,130109,130110,130111,130112,130113,130114,130115,130116,130117,130118,130119,130120,130121,130122,130123], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[330100,330101,330102,330103,330104,330105,330106,330107,330108,330109,330110,330111,330112,330113,330114,330115,330116,330117,330118,330119,330120,330121,330122,330123], visible=True, meshCount=24, arg4=100, delay=50) # Real
        self.set_agent(triggerIds=[18011], visible=False)
        self.set_agent(triggerIds=[18012], visible=False)
        self.set_agent(triggerIds=[18013], visible=False)
        self.set_agent(triggerIds=[18014], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[130100,130101,130102,130103,130104,130105,130106,130107,130108,130109,130110,130111,130112,130113,130114,130115,130116,130117,130118,130119,130120,130121,130122,130123], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
