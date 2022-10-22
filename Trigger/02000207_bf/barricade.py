""" trigger/02000207_bf/barricade.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2001]):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000207_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 차단()


class 차단(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=False, arg3=0, arg4=0, arg5=3)

    def on_tick(self) -> state.State:
        if user_value(key='BattleEnd', value=1):
            return 차단해제()


class 차단해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True, arg3=0, arg4=0, arg5=0)


