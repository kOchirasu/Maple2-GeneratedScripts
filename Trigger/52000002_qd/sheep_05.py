""" trigger/52000002_qd/sheep_05.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_effect(triggerIds=[615], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000615], arg2=0):
            return NPC교체()
        if not user_detected(boxIds=[101]):
            return NPC소멸()


class NPC교체(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        create_monster(spawnIds=[1095])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            set_interact_object(triggerIds=[10000615], state=2)
            return NPC이동()
        if not user_detected(boxIds=[101]):
            return NPC소멸()


class NPC이동(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=6)
        set_effect(triggerIds=[615], visible=True)
        move_npc(spawnId=1095, patrolName='MS2PatrolData_1095')
        set_conversation(type=1, spawnId=1095, script='$52000002_QD__SHEEP_05__0$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return NPC소멸()
        if not user_detected(boxIds=[101]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1095])

    def on_tick(self) -> state.State:
        if true():
            return 시작대기중()


