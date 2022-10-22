""" trigger/02000329_bf/bossgate.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[710]):
            return 사다리가이드()


class 사다리가이드(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=106, textId=20000060) # 다음 지역으로 이동하세요
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 대기()

    def on_exit(self):
        hide_guide_summary(entityId=106)


