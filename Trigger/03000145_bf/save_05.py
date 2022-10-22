""" trigger/03000145_bf/save_05.xml """
from common import *
import state


class 트리거초기화(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=1)
        set_mesh(triggerIds=[5001], visible=False, arg5=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000471], state=1)
        create_monster(spawnIds=[501], arg2=False)
        create_monster(spawnIds=[502], arg2=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000471], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_mesh(triggerIds=[5001], visible=True, arg5=1)
        destroy_monster(spawnIds=[501])
        destroy_monster(spawnIds=[502])
        create_monster(spawnIds=[511], arg2=False)
        create_monster(spawnIds=[512], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 도망갈준비1()


class 도망갈준비1(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=511, script='$03000145_BF__SAVE_05__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 도망갈준비2()


class 도망갈준비2(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_conversation(type=1, spawnId=512, script='$03000145_BF__SAVE_05__1$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 도망시작()


class 도망시작(state.State):
    def on_enter(self):
        move_npc(spawnId=511, patrolName='MS2PatrolData_511')
        move_npc(spawnId=512, patrolName='MS2PatrolData_512')

    def on_tick(self) -> state.State:
        if true():
            return 도망중()


class 도망중(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=4)
        set_conversation(type=1, spawnId=511, script='$03000145_BF__SAVE_05__2$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=512, script='$03000145_BF__SAVE_05__3$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 도망끝()


class 도망끝(state.State):
    def on_enter(self):
        set_timer(timerId='7', seconds=10)
        destroy_monster(spawnIds=[511])
        destroy_monster(spawnIds=[512])

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return 트리거초기화()


