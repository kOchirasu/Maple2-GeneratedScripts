""" trigger/02000252_bf/door_04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[175,176], visible=True)
        set_effect(triggerIds=[8037], visible=True)
        set_effect(triggerIds=[8038], visible=True)
        set_interact_object(triggerIds=[10000405], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000405], arg2=0):
            return 열기()


class 열기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_mesh(triggerIds=[175,176], visible=False)
        set_effect(triggerIds=[8037], visible=False)
        set_effect(triggerIds=[8038], visible=False)
        create_monster(spawnIds=[1014], arg2=False)
        set_conversation(type=1, spawnId=1014, script='$02000252_BF__DOOR_04__0$', arg4=2)
        move_npc(spawnId=1014, patrolName='MS2PatrolData_6')
        create_item(spawnIds=[1022])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 삭제()


class 삭제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1014])


