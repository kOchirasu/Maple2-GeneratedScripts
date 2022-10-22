""" trigger/02000091_bf/im_102.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000533], state=1)
        set_actor(triggerId=2102, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000533], arg2=0):
            return NPC이동()

    def on_exit(self):
        create_monster(spawnIds=[102])
        set_actor(triggerId=2102, visible=False, initialSequence='Idle_A')


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_Gull_102')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=1102, spawnIds=[102]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        set_timer(timerId='102', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='102'):
            return 시작대기중()


