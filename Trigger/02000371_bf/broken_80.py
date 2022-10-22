""" trigger/02000371_bf/broken_80.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111], visible=False, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[701], isEnable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 초대기5()


class 초대기5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 초대기30()


class 초대기30(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000384_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 스킬발동()


class 스킬발동(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003], visible=True, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[701], isEnable=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001,2101]):
            return 다리생성()


class 다리생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111], visible=True, arg3=0, arg4=100, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


