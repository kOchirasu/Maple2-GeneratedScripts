""" trigger/02020301_bf/3000064_phase_5_interect_04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200037,200038], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='Phase_5_Interect_04', value=1):
            return 시작()


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인터렉트_설정()


class 인터렉트_설정(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200037,200038], visible=True)
        set_interact_object(triggerIds=[10003104], state=1) # 4페이즈 인터렉트 오브젝트 생성
        set_visible_breakable_object(triggerIds=[5540], arg2=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10003104], arg2=0):
            return 인터렉트_동작()
        if user_value(key='Phase_5_Interect_04', value=0):
            return 대기()


class 인터렉트_동작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200037,200038], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 인터렉트_리셋()
        if user_value(key='Phase_5_Interect_04', value=0):
            return 대기()


class 인터렉트_리셋(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 인터렉트_설정()
        if user_value(key='Phase_5_Interect_04', value=0):
            return 대기()


