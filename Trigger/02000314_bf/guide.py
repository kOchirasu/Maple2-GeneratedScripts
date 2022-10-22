""" trigger/02000314_bf/guide.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[112]):
            return 타이어가이드()


class 타이어가이드(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003141, textId=20003141, duration=5000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[113]):
            return 타이어가이드2()


class 타이어가이드2(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003141, textId=20003141, duration=5000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 종료()


class 종료(state.State):
    pass


