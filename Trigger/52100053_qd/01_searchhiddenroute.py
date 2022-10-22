""" trigger/52100053_qd/01_searchhiddenroute.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # PortalOn
        set_user_value(key='PortalOn', value=0)
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PickRandomRoute()


class PickRandomRoute(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039701, textId=20039701, duration=4000) # 가이드 : 다른 방으로 이동할 수 있는 길을 찾으세요.

    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return BehindFireplace()
        if random_condition(rate=20):
            return BehindBookcase()
        if random_condition(rate=20):
            return FindKeyFromFabricbox()
        if random_condition(rate=20):
            return FindKeyFromCandle()
        if random_condition(rate=20):
            return FindKeyFromDocument()


class BehindBookcase(state.State):
    def on_enter(self):
        set_user_value(triggerId=3100, key='HiddenRouteOpen', value=2)
        set_user_value(triggerId=3200, key='HiddenRouteOpen', value=1)
        set_user_value(triggerId=3300, key='FindKey', value=2)
        set_user_value(triggerId=3400, key='FindKey', value=2)
        set_user_value(triggerId=3500, key='FindKey', value=2)


class BehindFireplace(state.State):
    def on_enter(self):
        set_user_value(triggerId=3100, key='HiddenRouteOpen', value=1)
        set_user_value(triggerId=3200, key='HiddenRouteOpen', value=2)
        set_user_value(triggerId=3300, key='FindKey', value=2)
        set_user_value(triggerId=3400, key='FindKey', value=2)
        set_user_value(triggerId=3500, key='FindKey', value=2)


class FindKeyFromFabricbox(state.State):
    def on_enter(self):
        set_user_value(triggerId=3100, key='HiddenRouteOpen', value=2)
        set_user_value(triggerId=3200, key='HiddenRouteOpen', value=2)
        set_user_value(triggerId=3300, key='FindKey', value=1)
        set_user_value(triggerId=3400, key='FindKey', value=2)
        set_user_value(triggerId=3500, key='FindKey', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='PortalOn', value=1):
            return PortalOn()


class FindKeyFromCandle(state.State):
    def on_enter(self):
        set_user_value(triggerId=3100, key='HiddenRouteOpen', value=2)
        set_user_value(triggerId=3200, key='HiddenRouteOpen', value=2)
        set_user_value(triggerId=3300, key='FindKey', value=2)
        set_user_value(triggerId=3400, key='FindKey', value=1)
        set_user_value(triggerId=3500, key='FindKey', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='PortalOn', value=1):
            return PortalOn()


class FindKeyFromDocument(state.State):
    def on_enter(self):
        set_user_value(triggerId=3100, key='HiddenRouteOpen', value=2)
        set_user_value(triggerId=3200, key='HiddenRouteOpen', value=2)
        set_user_value(triggerId=3300, key='FindKey', value=2)
        set_user_value(triggerId=3400, key='FindKey', value=2)
        set_user_value(triggerId=3500, key='FindKey', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='PortalOn', value=1):
            return PortalOn()


class PortalOn(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # PortalOn
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=False)


