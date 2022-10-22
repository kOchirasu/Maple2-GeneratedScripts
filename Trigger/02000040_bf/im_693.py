""" trigger/02000040_bf/im_693.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000693], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[108])


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000693], arg2=0):
            return 시간텀()

    def on_exit(self):
        destroy_monster(spawnIds=[108])
        create_monster(spawnIds=[1108])


class 시간텀(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1108, patrolName='MS2PatrolData_1108')
        set_conversation(type=1, spawnId=1108, script='$02000040_BF__IM_693__0$', arg4=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=1108, spawnIds=[1108]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1108])
        set_timer(timerId='1108', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1108'):
            return 시작대기중()


