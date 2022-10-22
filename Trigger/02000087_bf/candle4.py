""" trigger/02000087_bf/candle4.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000135], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000135], arg2=0):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104], arg2=False)
        move_npc(spawnId=104, patrolName='MS2PatrolData_204')
        set_timer(timerId='4', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 대화()


class 대화(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=104, script='$02000087_BF__CANDLE4__0$', arg4=2)
        set_timer(timerId='4', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104])
        set_timer(timerId='4', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 시작대기중()


