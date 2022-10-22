""" trigger/02000163_bf/01_trigger.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101])
        set_effect(triggerIds=[201], visible=True)
        set_effect(triggerIds=[202], visible=True)
        set_effect(triggerIds=[203], visible=True)
        set_effect(triggerIds=[204], visible=True)
        set_interact_object(triggerIds=[10000079], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000079], arg2=0):
            destroy_monster(spawnIds=[101])
            set_effect(triggerIds=[201], visible=False)
            set_effect(triggerIds=[202], visible=False)
            set_effect(triggerIds=[203], visible=False)
            set_effect(triggerIds=[204], visible=False)
            return 매킨생성()


class 매킨생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102])
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 매킨대사()


class 매킨대사(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000163_BF__01_TRIGGER__0$', arg4=3)
        move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=301, spawnIds=[102]):
            return 매킨이동302()


class 매킨이동302(state.State):
    def on_enter(self):
        create_item(spawnIds=[201], triggerId=0, itemId=10000079)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 매킨이동304()


class 매킨이동304(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=304, spawnIds=[102]):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        set_timer(timerId='1', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


