""" trigger/03009023_in/06.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000238], state=1)
        create_monster(spawnIds=[106], arg2=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000238], arg2=0):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=8)
        destroy_monster(spawnIds=[106])
        create_monster(spawnIds=[206], arg2=True)
        move_npc(spawnId=206, patrolName='MS2PatrolData_206')
        set_conversation(type=1, spawnId=206, script='$03009023_IN__06__0$', arg4=4, arg5=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[206])
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


