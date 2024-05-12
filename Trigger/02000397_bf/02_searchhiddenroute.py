""" trigger/02000397_bf/02_searchhiddenroute.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[920,921]) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9100]):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[920,921], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PickRandomRoute(self.ctx)


class PickRandomRoute(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 또 다른 방으로 이동할 수 있는 길을 찾으세요.
        self.show_guide_summary(entityId=20039702, textId=20039702, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return BehindWoodbox(self.ctx)
        if self.random_condition(rate=50):
            return BehindWardrope(self.ctx)


class BehindWoodbox(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=3600, key='HiddenRouteOpen', value=2)
        self.set_user_value(triggerId=3700, key='HiddenRouteOpen', value=1)


class BehindWardrope(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=3600, key='HiddenRouteOpen', value=1)
        self.set_user_value(triggerId=3700, key='HiddenRouteOpen', value=2)


initial_state = Wait
