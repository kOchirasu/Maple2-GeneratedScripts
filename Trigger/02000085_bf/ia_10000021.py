""" trigger/02000085_bf/ia_10000021.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000021], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000021], arg2=0):
            return NPC이동()

    def on_exit(self):
        create_monster(spawnIds=[101])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData1')
        set_conversation(type=1, spawnId=101, script='$02000085_BF__IA_10000021__0$', arg4=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=21, spawnIds=[101]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


