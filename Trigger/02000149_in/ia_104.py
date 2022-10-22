""" trigger/02000149_in/ia_104.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000193], state=1)
        set_actor(triggerId=204, visible=True, initialSequence='Sit_Chair_Idle_A')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000193], arg2=0):
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=204, visible=False, initialSequence='Sit_Chair_Idle_A')
        create_monster(spawnIds=[404])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=404, patrolName='MS2PatrolData_504')
        set_conversation(type=1, spawnId=404, script='$02000149_IN__IA_104__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=404, script='$02000149_IN__IA_104__1$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=604, spawnIds=[404]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[404])
        set_timer(timerId='1', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


