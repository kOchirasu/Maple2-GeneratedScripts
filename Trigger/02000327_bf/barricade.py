""" trigger/02000327_bf/barricade.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=False, arg3=0, arg4=0, arg5=0)

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
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=True, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 차단해제()


class 차단해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=False, arg3=0, arg4=200, arg5=2)


