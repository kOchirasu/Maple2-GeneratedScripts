""" trigger/02000013_bf/im_543.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000543], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()

    def on_exit(self):
        create_monster(spawnIds=[102])


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000543], arg2=0):
            return 시간텀()

    def on_exit(self):
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[1102])


class 시간텀(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1102, patrolName='MS2PatrolData_543')
        set_conversation(type=1, spawnId=1102, script='$02000013_BF__IM_543__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=543, spawnIds=[1102]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1102])
        set_timer(timerId='1', seconds=20)
        remove_balloon_talk(spawnId=1102)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()

