""" trigger/02000197_bf/im_562.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000562], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[101])


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000562], arg2=0):
            return NPC이동()

    def on_exit(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[1101])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1101, patrolName='MS2PatrolData_562')
        set_conversation(type=1, spawnId=1101, script='$02000197_BF__IM_562__0$', arg4=3)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=562, spawnIds=[1101]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1101])
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


