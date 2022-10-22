""" trigger/02000269_bf/im_103.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000678], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[103])


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000678], arg2=0):
            return 시간텀()

    def on_exit(self):
        destroy_monster(spawnIds=[103])
        create_monster(spawnIds=[1103])


class 시간텀(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1103, patrolName='MS2PatrolData_1103')
        set_conversation(type=1, spawnId=1103, script='$02000269_BF__IM_103__0$', arg4=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=1103, spawnIds=[1103]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1103])
        set_timer(timerId='1103', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1103'):
            return 시작대기중()

