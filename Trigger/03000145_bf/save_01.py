""" trigger/03000145_bf/save_01.xml """
from common import *
import state


class 트리거초기화(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=1)
        set_mesh(triggerIds=[1001], visible=False, arg5=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000467], state=1)
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000467], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_mesh(triggerIds=[1001], visible=True, arg5=1)
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[112], arg2=False)
        create_monster(spawnIds=[113], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 도망갈준비1()


class 도망갈준비1(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=111, script='$03000145_BF__SAVE_01__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 도망갈준비2()


class 도망갈준비2(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_conversation(type=1, spawnId=112, script='$03000145_BF__SAVE_01__1$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 도망갈준비3()


class 도망갈준비3(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=1)
        set_conversation(type=1, spawnId=113, script='$03000145_BF__SAVE_01__2$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 도망시작()


class 도망시작(state.State):
    def on_enter(self):
        move_npc(spawnId=111, patrolName='MS2PatrolData_111')
        move_npc(spawnId=112, patrolName='MS2PatrolData_112')
        move_npc(spawnId=113, patrolName='MS2PatrolData_113')

    def on_tick(self) -> state.State:
        if true():
            return 도망중()


class 도망중(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=3)
        set_conversation(type=1, spawnId=111, script='$03000145_BF__SAVE_01__3$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=112, script='$03000145_BF__SAVE_01__4$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=113, script='$03000145_BF__SAVE_01__5$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 도망끝()


class 도망끝(state.State):
    def on_enter(self):
        set_timer(timerId='7', seconds=10)
        destroy_monster(spawnIds=[111])
        destroy_monster(spawnIds=[112])
        destroy_monster(spawnIds=[113])

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return 트리거초기화()

