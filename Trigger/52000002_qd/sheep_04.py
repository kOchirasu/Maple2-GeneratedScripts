""" trigger/52000002_qd/sheep_04.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_effect(triggerIds=[614], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000616], arg2=0):
            return NPC교체()
        if not user_detected(boxIds=[101]):
            return NPC소멸()


class NPC교체(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_interact_object(triggerIds=[10000616], state=2)
        create_monster(spawnIds=[1094])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC이동()
        if not user_detected(boxIds=[101]):
            return NPC소멸()


class NPC이동(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=6)
        move_npc(spawnId=1094, patrolName='MS2PatrolData_1094')
        set_effect(triggerIds=[614], visible=True)
        set_conversation(type=1, spawnId=1094, script='$52000002_QD__SHEEP_04__0$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return NPC소멸()
        if not user_detected(boxIds=[101]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1094])

    def on_tick(self) -> state.State:
        if true():
            return 시작대기중()

