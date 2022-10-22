""" trigger/02000014_ad/ia_115.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000115], state=1)
        set_actor(triggerId=115, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000115], arg2=0):
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=115, visible=False, initialSequence='Dead_A')
        create_monster(spawnIds=[93], arg2=False)


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=93, patrolName='MS2PatrolData403')
        set_conversation(type=1, spawnId=93, script='$02000014_AD__IA_115__0$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=293, spawnIds=[93]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[93])
        set_timer(timerId='303', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='303'):
            return 시작대기중()


