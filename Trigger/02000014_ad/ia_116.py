""" trigger/02000014_ad/ia_116.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000116], state=1)
        set_actor(triggerId=116, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000116], arg2=0):
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=116, visible=False, initialSequence='Dead_A')
        create_monster(spawnIds=[94], arg2=False)


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=94, patrolName='MS2PatrolData404')
        set_conversation(type=1, spawnId=94, script='$02000014_AD__IA_116__0$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=294, spawnIds=[94]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[94])
        set_timer(timerId='304', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='304'):
            return 시작대기중()


