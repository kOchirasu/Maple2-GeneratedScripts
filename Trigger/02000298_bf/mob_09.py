""" trigger/02000298_bf/mob_09.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[607], visible=False)
        set_mesh(triggerIds=[3016,3017,3018,3019,3020], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3216,3217,3218,3219,3220], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[110]):
            create_monster(spawnIds=[1009], arg2=False)
            return 방호벽대기()
        if user_detected(boxIds=[111]):
            create_monster(spawnIds=[1009], arg2=False)
            return 방호벽대기()


class 방호벽대기(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1009]):
            return 방호벽해제()


class 방호벽해제(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)
        set_mesh(triggerIds=[3016,3017,3018,3019,3020], visible=False, arg3=0, arg4=0, arg5=5)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 번생성12()


class 번생성12(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1012], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1012]):
            return 방호벽해제2()


class 방호벽해제2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[607], visible=True)
        set_mesh(triggerIds=[3216,3217,3218,3219,3220], visible=False, arg3=0, arg4=0, arg5=5)
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


