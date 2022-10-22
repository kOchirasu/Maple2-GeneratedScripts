""" trigger/80000008_bonus/trigger_05.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[801,802,803,804,805], visible=False)
        set_effect(triggerIds=[806,807,808,809,810], visible=False)
        set_mesh(triggerIds=[201,202,203,204,205], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000212], state=1)

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
        set_timer(timerId='6', seconds=1, clearAtZero=True)
        set_effect(triggerIds=[801,802,803,804,805], visible=True)
        set_effect(triggerIds=[806,807,808,809,810], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 꽝()


class 꽝(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[104])
        destroy_monster(spawnIds=[105])
        set_mesh(triggerIds=[201,202,203,204,205], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000208], state=2)
        set_interact_object(triggerIds=[10000209], state=2)
        set_interact_object(triggerIds=[10000210], state=2)
        set_interact_object(triggerIds=[10000211], state=2)
        set_interact_object(triggerIds=[10000212], state=2)


