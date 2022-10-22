""" trigger/02000046_ad/eagle_07.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000299], state=1)
        set_actor(triggerId=207, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000299], arg2=0):
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if true():
            return NPC이동()

    def on_exit(self):
        set_actor(triggerId=207, visible=False, initialSequence='Dead_A')
        create_monster(spawnIds=[307], arg2=False)


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=307, patrolName='MS2PatrolData_207')
        set_conversation(type=1, spawnId=307, script='$02000046_AD__EAGLE_07__0$', arg4=2)
        set_timer(timerId='1', seconds=20)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[307])

    def on_tick(self) -> state.State:
        if true():
            return 시작대기중()


