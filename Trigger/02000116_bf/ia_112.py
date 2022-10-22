""" trigger/02000116_bf/ia_112.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000011], state=1)
        set_actor(triggerId=1121, visible=True, initialSequence='SOS_B')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[308])


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000011], arg2=0):
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=1121, visible=False, initialSequence='SOS_B')
        destroy_monster(spawnIds=[308])
        create_monster(spawnIds=[112])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=112, patrolName='MS2PatrolData112')
        set_conversation(type=1, spawnId=112, script='$02000116_BF__IA_112__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=112, script='$02000116_BF__IA_112__1$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=112, spawnIds=[112]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[112])
        set_timer(timerId='112', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='112'):
            return 시작대기중()


