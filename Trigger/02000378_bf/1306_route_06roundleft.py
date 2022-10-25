""" trigger/02000378_bf/1306_route_06roundleft.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[4013], visible=True, arg3=0, delay=0, scale=0) # PortalBarrier
        self.set_agent(triggerIds=[18061], visible=True)
        self.set_agent(triggerIds=[18062], visible=True)
        self.set_effect(triggerIds=[5006], visible=False) # 06Round_BridgeApp
        self.set_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[330600,330601,330602,330603,330604,330605,330606,330607,330608,330609,330610,330611,330612,330613,330614,330615,330616,330617,330618,330619,330620,330621,330622,330623,330624,330625], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9000, boxId=1):
            return StartDazzling01(self.ctx)


class StartDazzling01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(common.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=False, meshCount=26, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(common.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=False, meshCount=26, arg4=0, delay=0) # Fake


class MakeTrue(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5006], visible=True) # 06Round_BridgeApp
        self.set_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[330600,330601,330602,330603,330604,330605,330606,330607,330608,330609,330610,330611,330612,330613,330614,330615,330616,330617,330618,330619,330620,330621,330622,330623,330624,330625], visible=True, meshCount=26, arg4=100, delay=50) # Real
        self.set_agent(triggerIds=[18061], visible=False)
        self.set_agent(triggerIds=[18062], visible=False)
        self.set_portal(portalId=13, visible=True, enable=True, minimapVisible=False)
        self.set_mesh(triggerIds=[4013], visible=False, arg3=0, delay=0, scale=0) # PortalBarrier

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
