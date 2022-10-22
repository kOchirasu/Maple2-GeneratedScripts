""" trigger/02000137_bf/ia_47.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000047], state=1)
        create_monster(spawnIds=[147])

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000047], arg2=0):
            return NPC탈출()

    def on_exit(self):
        destroy_monster(spawnIds=[147])


class NPC탈출(state.State):
    def on_enter(self):
        create_monster(spawnIds=[148])
        set_conversation(type=1, spawnId=148, script='$02000137_BF__IA_47__0$', arg4=2)
        set_timer(timerId='1', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            destroy_monster(spawnIds=[148])
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


