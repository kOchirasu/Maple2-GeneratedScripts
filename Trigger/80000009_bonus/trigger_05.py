""" trigger/80000009_bonus/trigger_05.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[801,802,803,804,805,806,807,808,809,810], visible=False)
        set_interact_object(triggerIds=[10000212], state=1)
        set_mesh(triggerIds=[201,202,203,204,205], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000212], arg2=0):
            return 소환()


class 소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105], arg2=False)
        move_npc(spawnId=105, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=401, spawnIds=[105]):
            return 몬스터소멸()


class 몬스터소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105])
        set_timer(timerId='5', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 아이템()


class 아이템(state.State):
    def on_enter(self):
        create_item(spawnIds=[505])
        set_effect(triggerIds=[810], visible=True)
        set_mesh(triggerIds=[205], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000212], state=2)


