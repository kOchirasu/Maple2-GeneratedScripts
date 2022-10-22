""" trigger/02000177_bf/guide.xml """
from common import *
import state


class guide(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return Guide_Climb()


class Guide_Climb(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20001771, textId=20001771, duration=4000)

    def on_tick(self) -> state.State:
        if count_users(boxId=703, boxId=1):
            return Guide_Climb_02()


class Guide_Climb_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20001771, textId=20001771, duration=4000)


