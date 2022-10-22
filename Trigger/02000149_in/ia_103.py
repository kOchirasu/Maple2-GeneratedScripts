""" trigger/02000149_in/ia_103.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000192], state=1)
        set_actor(triggerId=203, visible=True, initialSequence='Sit_Chair_Idle_A')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000192], arg2=0):
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=203, visible=False, initialSequence='Sit_Chair_Idle_A')
        create_monster(spawnIds=[403])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=403, patrolName='MS2PatrolData_503')
        set_conversation(type=1, spawnId=403, script='$02000149_IN__IA_103__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=403, script='$02000149_IN__IA_103__1$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=603, spawnIds=[403]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[403])
        set_timer(timerId='1', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


