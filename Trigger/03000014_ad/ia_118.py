""" trigger/03000014_ad/ia_118.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000118], state=1)
        set_actor(triggerId=118, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000118], arg2=0):
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=118, visible=False, initialSequence='Dead_A')
        create_monster(spawnIds=[96], arg2=False)


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=96, patrolName='MS2PatrolData406')
        set_conversation(type=1, spawnId=96, script='$03000014_AD__IA_118__0$', arg4=4)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=296, spawnIds=[96]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[96])
        set_timer(timerId='306', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='306'):
            return 시작대기중()


