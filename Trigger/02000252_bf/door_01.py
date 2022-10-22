""" trigger/02000252_bf/door_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[169,170], visible=True)
        set_effect(triggerIds=[8031], visible=True)
        set_effect(triggerIds=[8032], visible=True)
        set_interact_object(triggerIds=[10000401], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000401], arg2=0):
            return 열기()


class 열기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_effect(triggerIds=[8031], visible=False)
        set_effect(triggerIds=[8032], visible=False)
        set_mesh(triggerIds=[169,170], visible=False)
        create_monster(spawnIds=[1012], arg2=True)
        set_conversation(type=1, spawnId=1012, script='$02000252_BF__DOOR_01__0$', arg4=2)
        move_npc(spawnId=1012, patrolName='MS2PatrolData_3')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 삭제()


class 삭제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1012])


