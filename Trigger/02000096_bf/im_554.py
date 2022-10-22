""" trigger/02000096_bf/im_554.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000554], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000554], arg2=0):
            return NPC이동()

    def on_exit(self):
        create_monster(spawnIds=[103])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_554')
        set_conversation(type=1, spawnId=103, script='$02000096_BF__IM_554__0$', arg4=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=554, spawnIds=[103]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


