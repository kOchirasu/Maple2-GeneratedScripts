""" trigger/02000483_bf/02_searchhiddenroute.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[920,921]) # Mob

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[920,921], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PickRandomRoute()


class PickRandomRoute(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039702, textId=20039702, duration=4000) # 가이드 : 또 다른 방으로 이동할 수 있는 길을 찾으세요.

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return BehindWoodbox()
        if random_condition(rate=50):
            return BehindWardrope()


class BehindWoodbox(state.State):
    def on_enter(self):
        set_user_value(triggerId=3600, key='HiddenRouteOpen', value=2)
        set_user_value(triggerId=3700, key='HiddenRouteOpen', value=1)


class BehindWardrope(state.State):
    def on_enter(self):
        set_user_value(triggerId=3600, key='HiddenRouteOpen', value=1)
        set_user_value(triggerId=3700, key='HiddenRouteOpen', value=2)


