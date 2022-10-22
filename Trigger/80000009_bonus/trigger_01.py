""" trigger/80000009_bonus/trigger_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000208], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000208], arg2=0):
            return 소환()


class 소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=401, spawnIds=[101]):
            return 몬스터소멸()


class 몬스터소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 아이템()


class 아이템(state.State):
    def on_enter(self):
        create_item(spawnIds=[504])

    def on_tick(self) -> state.State:
        if true():
            return 대기()


