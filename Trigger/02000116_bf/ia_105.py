""" trigger/02000116_bf/ia_105.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000004], state=1)
        set_actor(triggerId=1051, visible=True, initialSequence='SOS_B')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[301])


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000004], arg2=0):
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=1051, visible=False, initialSequence='SOS_B')
        destroy_monster(spawnIds=[301])
        create_monster(spawnIds=[105])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='MS2PatrolData105')
        set_conversation(type=1, spawnId=105, script='$02000116_BF__IA_105__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=105, script='$02000116_BF__IA_105__1$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=105, spawnIds=[105]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105])
        set_timer(timerId='105', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='105'):
            return 시작대기중()


