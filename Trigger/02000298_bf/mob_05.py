""" trigger/02000298_bf/mob_05.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_mesh(triggerIds=[3006,3007,3008,3009,3010], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3206,3207,3208,3209,3210], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            create_monster(spawnIds=[1005], arg2=False)
            return 방호벽대기()
        if user_detected(boxIds=[103]):
            create_monster(spawnIds=[1005], arg2=False)
            return 방호벽대기()


class 방호벽대기(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1005]):
            return 방호벽해제()


class 방호벽해제(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        set_mesh(triggerIds=[3006,3007,3008,3009,3010], visible=False, arg3=0, arg4=0, arg5=5)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 번생성10()


class 번생성10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1010], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1010]):
            return 방호벽해제2()


class 방호벽해제2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)
        set_mesh(triggerIds=[3206,3207,3208,3209,3210], visible=False, arg3=0, arg4=0, arg5=5)
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


