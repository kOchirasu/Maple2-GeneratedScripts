""" trigger/80000009_bonus/trigger_04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000211], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000211], arg2=0):
            return 소환()


class 소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104], arg2=False)
        move_npc(spawnId=104, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=401, spawnIds=[104]):
            return 몬스터소멸()


class 몬스터소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104])
        set_timer(timerId='4', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 아이템()


class 아이템(state.State):
    def on_enter(self):
        create_item(spawnIds=[502])

    def on_tick(self) -> state.State:
        if true():
            return 대기()


