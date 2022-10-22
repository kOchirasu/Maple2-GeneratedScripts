""" trigger/99999985_plantest_08/ia_110.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000009], state=1)
        set_actor(triggerId=1101, visible=True, initialSequence='SOS_B')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[306])


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000009], arg2=0):
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=1101, visible=False, initialSequence='SOS_B')
        destroy_monster(spawnIds=[306])
        create_monster(spawnIds=[110])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=110, patrolName='MS2PatrolData110')
        set_conversation(type=1, spawnId=110, script='$02000116_BF__IA_110__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=110, script='$02000116_BF__IA_110__1$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=110, spawnIds=[110]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[110])
        set_timer(timerId='110', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='110'):
            return 시작대기중()


