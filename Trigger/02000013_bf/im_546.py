""" trigger/02000013_bf/im_546.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000546], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[105])


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000546], arg2=0):
            return 시간텀()

    def on_exit(self):
        destroy_monster(spawnIds=[105])
        create_monster(spawnIds=[1105])


class 시간텀(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1105, patrolName='MS2PatrolData_546')
        set_conversation(type=1, spawnId=1105, script='$02000013_BF__IM_546__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=1105, script='$02000013_BF__IM_546__1$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=546, spawnIds=[1105]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1105])
        set_timer(timerId='1', seconds=20)
        remove_balloon_talk(spawnId=1105)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


