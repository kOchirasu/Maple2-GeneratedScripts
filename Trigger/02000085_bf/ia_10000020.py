""" trigger/02000085_bf/ia_10000020.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000020], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000020], arg2=0):
            return NPC이동()

    def on_exit(self):
        create_monster(spawnIds=[100])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=100, patrolName='MS2PatrolData0')
        set_conversation(type=1, spawnId=100, script='$02000085_BF__IA_10000020__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=20, spawnIds=[100]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[100])
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


