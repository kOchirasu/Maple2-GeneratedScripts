""" trigger/02000396_bf/06_toroom_false.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001135], state=0) # ToRoom_False
        set_user_value(key='ToRoomFalse', value=0)
        set_user_value(key='AnotherGuide', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='ToRoomFalse', value=1):
            return ToRoomFalse()


class ToRoomFalse(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001135], state=1) # ToRoom_False

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001135], arg2=0):
            return NoticeDelay()


class NoticeDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=5, key='AnotherGuide', value=1)
        set_user_value(triggerId=7, key='AnotherGuide', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NoticeOn()


class NoticeOn(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039604, textId=20039604) # 가이드 : 문이 안쪽에서 굳게 잠겨 있습니다.

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
        hide_guide_summary(entityId=20039604)
        set_user_value(triggerId=5, key='AnotherGuide', value=0)
        set_user_value(triggerId=7, key='AnotherGuide', value=0)


