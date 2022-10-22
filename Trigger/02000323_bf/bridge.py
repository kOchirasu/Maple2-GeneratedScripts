""" trigger/02000323_bf/bridge.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[99]):
            return 발판01()


class 발판01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=False, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 재생성()


class 재생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=True, arg3=0, arg4=0, arg5=0)


