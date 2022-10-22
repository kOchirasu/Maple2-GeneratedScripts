""" trigger/52000076_qd/fog.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000813], state=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=136, spawnIds=[2006]):
            return 시작대기중()


class 시작대기중(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1098])
        set_effect(triggerIds=[600], visible=False) # fog 500
        set_effect(triggerIds=[602], visible=False) # fog 1500
        set_interact_object(triggerIds=[10000813], state=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1098]):
            return 포그()


class 포그(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        set_interact_object(triggerIds=[10000813], state=1)
        show_guide_summary(entityId=20003494, textId=20003494)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000813], arg2=0):
            return 대기시간()
        if monster_dead(boxIds=[1099]):
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20003494)
        set_effect(triggerIds=[602], visible=True)
        set_interact_object(triggerIds=[10000813], state=0)
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 시작대기중()


