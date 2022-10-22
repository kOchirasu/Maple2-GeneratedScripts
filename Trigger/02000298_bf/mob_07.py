""" trigger/02000298_bf/mob_07.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[606], visible=False)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3211,3212,3213,3214,3215], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            create_monster(spawnIds=[1007], arg2=False)
            return 방호벽대기()
        if user_detected(boxIds=[107]):
            create_monster(spawnIds=[1007], arg2=False)
            return 방호벽대기()


class 방호벽대기(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1007]):
            return 방호벽해제()


class 방호벽해제(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205], visible=False, arg3=0, arg4=0, arg5=5)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 번생성11()


class 번생성11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1011], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1011]):
            return 방호벽해제2()


class 방호벽해제2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[606], visible=True)
        set_mesh(triggerIds=[3211,3212,3213,3214,3215], visible=False, arg3=0, arg4=0, arg5=5)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1800000'):
            return None # Missing State: 종료2


