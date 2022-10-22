""" trigger/99999985_plantest_08/ia_111.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000010], state=1)
        set_actor(triggerId=1111, visible=True, initialSequence='SOS_B')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[307])


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000010], arg2=0):
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=1111, visible=False, initialSequence='SOS_B')
        destroy_monster(spawnIds=[307])
        create_monster(spawnIds=[111])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=111, patrolName='MS2PatrolData111')
        set_conversation(type=1, spawnId=111, script='$02000116_BF__IA_111__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=111, script='$02000116_BF__IA_111__1$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=111, spawnIds=[111]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111])
        set_timer(timerId='111', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='111'):
            return 시작대기중()


