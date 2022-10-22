""" trigger/02000116_bf/ia_106.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000005], state=1)
        set_actor(triggerId=1061, visible=True, initialSequence='SOS_B')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[302])


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000005], arg2=0):
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=1061, visible=False, initialSequence='SOS_B')
        destroy_monster(spawnIds=[302])
        create_monster(spawnIds=[106])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=106, patrolName='MS2PatrolData106')
        set_conversation(type=1, spawnId=106, script='$02000116_BF__IA_106__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=106, script='$02000116_BF__IA_106__1$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=106, spawnIds=[106]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[106])
        set_timer(timerId='106', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='106'):
            return 시작대기중()


