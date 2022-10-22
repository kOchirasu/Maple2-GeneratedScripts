""" trigger/52100301_qd/3000054_phase_4_interect_04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200027,200028], visible=False)
        set_interact_object(triggerIds=[10003114], state=2) # 4페이즈 인터렉트 오브젝트 생성

    def on_tick(self) -> state.State:
        if user_value(key='Phase_4_Interect_04', value=1):
            return 시작()


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 인터렉트_설정()
        if user_value(key='Phase_4_Interect_04', value=0):
            return 대기()


class 인터렉트_설정(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200027,200028], visible=True)
        set_interact_object(triggerIds=[10003114], state=1) # 4페이즈 인터렉트 오브젝트 생성

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10003114], arg2=0):
            return 인터렉트_동작()
        if user_value(key='Phase_4_Interect_04', value=0):
            return 대기()


class 인터렉트_동작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200027,200028], visible=False)
        set_ai_extra_data(key='Phase_4_Sub_Bomb_4', value=1, isModify=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 인터렉트_리셋()
        if user_value(key='Phase_4_Interect_04', value=0):
            return 대기()


class 인터렉트_리셋(state.State):
    def on_enter(self):
        set_ai_extra_data(key='Phase_4_Sub_Bomb_4', value=0, isModify=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 인터렉트_설정()
        if user_value(key='Phase_4_Interect_04', value=0):
            return 대기()


