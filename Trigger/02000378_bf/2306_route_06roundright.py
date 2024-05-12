""" trigger/02000378_bf/2306_route_06roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=14, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[4014], visible=True, arg3=0, delay=0, scale=0) # PortalBarrier
        self.set_agent(triggerIds=[28061], visible=True)
        self.set_agent(triggerIds=[28062], visible=True)
        self.set_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[430600,430601,430602,430603,430604,430605,430606,430607,430608,430609,430610,430611,430612,430613,430614,430615,430616,430617,430618,430619], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, meshCount=20, arg4=0, delay=0)
        # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, meshCount=20, arg4=0, delay=0)
        # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5006], visible=True) # 06Round_BridgeApp
        self.set_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[430600,430601,430602,430603,430604,430605,430606,430607,430608,430609,430610,430611,430612,430613,430614,430615,430616,430617,430618,430619], visible=True, meshCount=20, arg4=0, delay=50) # Real
        self.set_agent(triggerIds=[28061], visible=False)
        self.set_agent(triggerIds=[28062], visible=False)
        self.set_portal(portalId=14, visible=True, enable=True, minimapVisible=False)
        self.set_mesh(triggerIds=[4014], visible=False, arg3=0, delay=0, scale=0) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
