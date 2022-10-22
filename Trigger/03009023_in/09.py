""" trigger/03009023_in/09.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000241], state=1)
        create_monster(spawnIds=[109], arg2=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000241], arg2=0):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)
        destroy_monster(spawnIds=[109])
        create_monster(spawnIds=[209], arg2=True)
        move_npc(spawnId=209, patrolName='MS2PatrolData_209')
        set_conversation(type=1, spawnId=209, script='$03009023_IN__09__0$', arg4=4, arg5=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[209])
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


