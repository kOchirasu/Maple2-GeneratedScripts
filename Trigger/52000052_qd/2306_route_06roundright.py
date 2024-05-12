""" trigger/52000052_qd/2306_route_06roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=14, visible=False, enable=False, minimap_visible=False)
        self.set_mesh(trigger_ids=[4014], visible=True, start_delay=0, interval=0, fade=0) # PortalBarrier
        self.set_agent(trigger_ids=[28061], visible=True)
        self.set_agent(trigger_ids=[28062], visible=True)
        self.set_mesh(trigger_ids=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, start_delay=0, interval=0, fade=0) # Fake
        self.set_mesh(trigger_ids=[430600,430601,430602,430603,430604,430605,430606,430607,430608,430609,430610,430611,430612,430613,430614,430615,430616,430617,430618,430619], visible=False, start_delay=0, interval=0, fade=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected') >= 1:
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue') >= 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') >= 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, start_delay=20, interval=0, fade=0) # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=True, start_delay=6, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue') >= 1:
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse') >= 1:
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, start_delay=20, interval=0, fade=0) # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5006], visible=True) # 06Round_BridgeApp
        self.set_mesh(trigger_ids=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, start_delay=0, interval=0, fade=5) # Fake
        self.set_random_mesh(trigger_ids=[430600,430601,430602,430603,430604,430605,430606,430607,430608,430609,430610,430611,430612,430613,430614,430615,430616,430617,430618,430619], visible=True, start_delay=20, interval=0, fade=50) # Real
        self.set_agent(trigger_ids=[28061], visible=False)
        self.set_agent(trigger_ids=[28062], visible=False)
        self.set_portal(portal_id=14, visible=True, enable=True, minimap_visible=False)
        self.set_mesh(trigger_ids=[4014], visible=False, start_delay=0, interval=0, fade=0) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, start_delay=0, interval=0, fade=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
