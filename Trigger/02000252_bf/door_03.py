""" trigger/02000252_bf/door_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[173,174], visible=True)
        set_effect(triggerIds=[8035], visible=True)
        set_effect(triggerIds=[8036], visible=True)
        set_interact_object(triggerIds=[10000404], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000404], arg2=0):
            return 열기()


class 열기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_mesh(triggerIds=[173,174], visible=False)
        set_effect(triggerIds=[8035], visible=False)
        set_effect(triggerIds=[8036], visible=False)
        create_monster(spawnIds=[1013], arg2=True)
        set_conversation(type=1, spawnId=1013, script='$02000252_BF__DOOR_03__0$', arg4=2)
        move_npc(spawnId=1013, patrolName='MS2PatrolData_6')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 삭제()


class 삭제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1013])


