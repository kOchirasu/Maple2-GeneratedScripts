""" trigger/02000087_bf/candle2.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000134], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000134], arg2=0):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_202')
        set_conversation(type=1, spawnId=102, script='$02000087_BF__CANDLE2__0$', arg4=2)
        set_timer(timerId='2', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        set_timer(timerId='2', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 시작대기중()


