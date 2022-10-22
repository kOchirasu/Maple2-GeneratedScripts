""" trigger/03000049_bf/10001582_eagle_505.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000333], state=1)
        set_actor(triggerId=505, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000333], arg2=0):
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if true():
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=505, visible=False, initialSequence='Idle_A')
        create_monster(spawnIds=[5005], arg2=False)


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=5005, patrolName='MS2PatrolData_505')
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5005])
        set_timer(timerId='2', seconds=50)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 시작대기중()

