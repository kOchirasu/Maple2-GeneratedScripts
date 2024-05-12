""" trigger/02000378_bf/2309_route_09roundright.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=16, visible=False, enable=False, minimap_visible=False)
        self.set_mesh(trigger_ids=[4016], visible=True, start_delay=0, interval=0, fade=0) # PortalBarrier
        self.set_agent(trigger_ids=[28091], visible=True)
        self.set_agent(trigger_ids=[28092], visible=True)
        self.set_mesh(trigger_ids=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, start_delay=0, interval=0, fade=0) # Fake
        self.set_mesh(trigger_ids=[430900,430901,430902,430903,430904,430905,430906,430907,430908,430909], visible=False, start_delay=0, interval=0, fade=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=True, start_delay=3, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, start_delay=10, interval=0, fade=0)
        # Fake


class StartDazzlingRandom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(trigger_ids=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=True, start_delay=3, interval=100, fade=500) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self) -> None:
        self.set_random_mesh(trigger_ids=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, start_delay=10, interval=0, fade=0)
        # Fake


class MakeTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5009], visible=True) # 09Round_BridgeApp
        self.set_mesh(trigger_ids=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, start_delay=0, interval=0, fade=5) # Fake
        self.set_random_mesh(trigger_ids=[430900,430901,430902,430903,430904,430905,430906,430907,430908,430909], visible=True, start_delay=10, interval=0, fade=50) # Real
        self.set_agent(trigger_ids=[28091], visible=False)
        self.set_agent(trigger_ids=[28092], visible=False)
        self.set_portal(portal_id=16, visible=True, enable=True, minimap_visible=False)
        self.set_mesh(trigger_ids=[4016], visible=False, start_delay=0, interval=0, fade=0) # PortalBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class MakeFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, start_delay=0, interval=0, fade=5) # Fake

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
