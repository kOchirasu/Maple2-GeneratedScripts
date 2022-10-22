""" trigger/02000040_bf/im_687.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000687], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[102])


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000687], arg2=0):
            return 시간텀()

    def on_exit(self):
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[1102])


class 시간텀(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1102, patrolName='MS2PatrolData_1102')
        set_conversation(type=1, spawnId=1102, script='$02000040_BF__IM_687__0$', arg4=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=1102, spawnIds=[1102]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1102])
        set_timer(timerId='1102', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1102'):
            return 시작대기중()


