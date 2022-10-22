""" trigger/03000014_ad/ia_113.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000113], state=1)
        set_actor(triggerId=113, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000113], arg2=0):
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=113, visible=False, initialSequence='Dead_A')
        create_monster(spawnIds=[91], arg2=False)


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=91, patrolName='MS2PatrolData401')
        set_conversation(type=1, spawnId=91, script='$03000014_AD__IA_113__0$', arg4=4)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=291, spawnIds=[91]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[91])
        set_timer(timerId='301', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='301'):
            return 시작대기중()


