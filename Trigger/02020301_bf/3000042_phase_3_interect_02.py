""" trigger/02020301_bf/3000042_phase_3_interect_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200011,200012,200013,200014], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='Phase_3_Interect_02', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        add_buff(boxIds=[1003], skillId=62100168, level=1) # 포탑 기절 이뮨

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인터렉트_설정()


class 인터렉트_설정(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200011,200012,200013,200014], visible=True)
        set_interact_object(triggerIds=[10003121], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10003121], arg2=0):
            return 인터렉트_동작()
        if user_value(key='Phase_3_Interect_02', value=0):
            return 대기()


class 인터렉트_동작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200011,200012,200013,200014], visible=False)
        set_ai_extra_data(key='Shoot_Cannon_2', value=1, isModify=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 인터렉트_리셋()
        if user_value(key='Phase_3_Interect_02', value=0):
            return 대기()


class 인터렉트_리셋(state.State):
    def on_enter(self):
        set_ai_extra_data(key='Shoot_Cannon_2', value=0, isModify=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 인터렉트_설정()
        if user_value(key='Phase_3_Interect_02', value=0):
            return 대기()


