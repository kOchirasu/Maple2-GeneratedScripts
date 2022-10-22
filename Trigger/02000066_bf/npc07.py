""" trigger/02000066_bf/npc07.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[605], visible=False)
        set_actor(triggerId=207, visible=False, initialSequence='Dead_A')
        set_interact_object(triggerIds=[10000375], state=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return NPC생성()


class NPC생성(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        create_monster(spawnIds=[2007], arg2=False)
        set_interact_object(triggerIds=[10000375], state=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC생성조건()


class NPC생성조건(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2007]):
            set_effect(triggerIds=[605], visible=True)
            show_guide_summary(entityId=20000663, textId=20000663)
            play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        destroy_monster(spawnIds=[2007])

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            hide_guide_summary(entityId=20000663)
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_enter(self):
        set_actor(triggerId=207, visible=True, initialSequence='Dead_A')
        set_interact_object(triggerIds=[10000375], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000375], arg2=0):
            return 부활()


class 부활(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        create_monster(spawnIds=[2007], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC대사()


class NPC대사(state.State):
    def on_enter(self):
        set_actor(triggerId=207, visible=False, initialSequence='Dead_A')
        set_conversation(type=1, spawnId=2007, script='$02000066_BF__NPC07__1$', arg4=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2007]):
            return NPC생성조건()


