""" trigger/03000145_bf/save_03.xml """
from common import *
import state


class 트리거초기화(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=1)
        set_mesh(triggerIds=[3001], visible=False, arg5=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000469], state=1)
        create_monster(spawnIds=[301], arg2=False)
        create_monster(spawnIds=[302], arg2=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000469], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_mesh(triggerIds=[3001], visible=True, arg5=1)
        destroy_monster(spawnIds=[301])
        destroy_monster(spawnIds=[302])
        create_monster(spawnIds=[311], arg2=False)
        create_monster(spawnIds=[312], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 도망갈준비1()


class 도망갈준비1(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=311, script='$03000145_BF__SAVE_03__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 도망갈준비2()


class 도망갈준비2(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_conversation(type=1, spawnId=312, script='$03000145_BF__SAVE_03__1$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 도망시작()


class 도망시작(state.State):
    def on_enter(self):
        move_npc(spawnId=311, patrolName='MS2PatrolData_311')
        move_npc(spawnId=312, patrolName='MS2PatrolData_312')

    def on_tick(self) -> state.State:
        if true():
            return 도망중()


class 도망중(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=3)
        set_conversation(type=1, spawnId=311, script='$03000145_BF__SAVE_03__2$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=312, script='$03000145_BF__SAVE_03__3$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 도망끝()


class 도망끝(state.State):
    def on_enter(self):
        set_timer(timerId='7', seconds=10)
        destroy_monster(spawnIds=[311])
        destroy_monster(spawnIds=[312])

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return 트리거초기화()


