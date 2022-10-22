""" trigger/02000066_bf/gate05.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[3005])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=False)
        set_interact_object(triggerIds=[10000337], state=0)
        create_monster(spawnIds=[3005], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3005]):
            return 게이트열림()


class 게이트열림(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_interact_object(triggerIds=[10000337], state=1)
        set_effect(triggerIds=[604], visible=True)
        show_guide_summary(entityId=20000664, textId=20000664)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            hide_guide_summary(entityId=20000664)
            return 게이트닫힘()


class 게이트닫힘(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000337], arg2=0):
            return 생성()


