""" trigger/02000396_bf/07_totower_false.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001136], state=0) # ToTower_False
        set_user_value(key='ToTowerFalse', value=0)
        set_user_value(key='AnotherGuide', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='ToTowerFalse', value=1):
            return ToTowerFalse()


class ToTowerFalse(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001136], state=1) # ToTower_False

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001136], arg2=0):
            return NoticeDelay()


class NoticeDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=5, key='AnotherGuide', value=1)
        set_user_value(triggerId=6, key='AnotherGuide', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NoticeOn()


class NoticeOn(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039605, textId=20039605) # 가이드 : 철창은 자물쇠로 단단히 묶여 있습니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CloseGuide02()
        if user_value(key='AnotherGuide', value=1):
            return CloseGuide01()


class CloseGuide01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return CloseGuide02()


class CloseGuide02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20039605)
        set_user_value(triggerId=5, key='AnotherGuide', value=0)
        set_user_value(triggerId=6, key='AnotherGuide', value=0)


