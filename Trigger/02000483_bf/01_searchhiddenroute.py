""" trigger/02000483_bf/01_searchhiddenroute.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=False) # PortalOn
        self.set_user_value(key='PortalOn', value=0)
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PickRandomRoute(self.ctx)


class PickRandomRoute(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 다른 방으로 이동할 수 있는 길을 찾으세요.
        self.show_guide_summary(entityId=20039701, textId=20039701, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return BehindFireplace(self.ctx)
        if self.random_condition(rate=20):
            return BehindBookcase(self.ctx)
        if self.random_condition(rate=20):
            return FindKeyFromFabricbox(self.ctx)
        if self.random_condition(rate=20):
            return FindKeyFromCandle(self.ctx)
        if self.random_condition(rate=20):
            return FindKeyFromDocument(self.ctx)


class BehindBookcase(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=3100, key='HiddenRouteOpen', value=2)
        self.set_user_value(triggerId=3200, key='HiddenRouteOpen', value=1)
        self.set_user_value(triggerId=3300, key='FindKey', value=2)
        self.set_user_value(triggerId=3400, key='FindKey', value=2)
        self.set_user_value(triggerId=3500, key='FindKey', value=2)


class BehindFireplace(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=3100, key='HiddenRouteOpen', value=1)
        self.set_user_value(triggerId=3200, key='HiddenRouteOpen', value=2)
        self.set_user_value(triggerId=3300, key='FindKey', value=2)
        self.set_user_value(triggerId=3400, key='FindKey', value=2)
        self.set_user_value(triggerId=3500, key='FindKey', value=2)


class FindKeyFromFabricbox(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=3100, key='HiddenRouteOpen', value=2)
        self.set_user_value(triggerId=3200, key='HiddenRouteOpen', value=2)
        self.set_user_value(triggerId=3300, key='FindKey', value=1)
        self.set_user_value(triggerId=3400, key='FindKey', value=2)
        self.set_user_value(triggerId=3500, key='FindKey', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PortalOn', value=1):
            return PortalOn(self.ctx)


class FindKeyFromCandle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=3100, key='HiddenRouteOpen', value=2)
        self.set_user_value(triggerId=3200, key='HiddenRouteOpen', value=2)
        self.set_user_value(triggerId=3300, key='FindKey', value=2)
        self.set_user_value(triggerId=3400, key='FindKey', value=1)
        self.set_user_value(triggerId=3500, key='FindKey', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PortalOn', value=1):
            return PortalOn(self.ctx)


class FindKeyFromDocument(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=3100, key='HiddenRouteOpen', value=2)
        self.set_user_value(triggerId=3200, key='HiddenRouteOpen', value=2)
        self.set_user_value(triggerId=3300, key='FindKey', value=2)
        self.set_user_value(triggerId=3400, key='FindKey', value=2)
        self.set_user_value(triggerId=3500, key='FindKey', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PortalOn', value=1):
            return PortalOn(self.ctx)


class PortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # PortalOn
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=False)


initial_state = Wait
