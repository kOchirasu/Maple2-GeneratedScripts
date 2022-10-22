""" trigger/02010051_bf/barricade.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[99]):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000384_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 차단()


class 차단(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506], visible=True, arg3=0, arg4=0, arg5=0) # Gate Close grating
        set_mesh(triggerIds=[1511,1512,1513], visible=False, arg3=0, arg4=0, arg5=0) # Gate Open grating

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 차단해제()


class 차단해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506], visible=False, arg3=0, arg4=0, arg5=10) # Gate Close grating
        set_mesh(triggerIds=[1511,1512,1513], visible=True, arg3=1, arg4=0, arg5=0) # Gate Open grating

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 종료(state.State):
    pass


