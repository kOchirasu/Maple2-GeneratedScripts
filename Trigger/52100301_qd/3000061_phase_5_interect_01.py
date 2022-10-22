""" trigger/52100301_qd/3000061_phase_5_interect_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200031,200032], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='Phase_5_Interect_01', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52100301_QD__3000061_PHASE_5_INTERECT_01__0$', arg3='4000')
        create_monster(spawnIds=[999], arg2=False) # 탑승 아르케온 등장(연출용)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 탈것_등장()


class 탈것_등장(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10003126], state=1)
        destroy_monster(spawnIds=[999])

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10003126], arg2=0):
            return 인터렉트_동작()
        if user_value(key='Phase_5_Interect_01', value=0):
            return 대기()


class 인터렉트_동작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 인터렉트_리셋()
        if user_value(key='Phase_5_Interect_01', value=0):
            return 대기()


class 인터렉트_리셋(state.State):
    def on_tick(self) -> state.State:
        if check_any_user_additional_effect(boxId=0, additionalEffectId=62100152, level=1):
            return 리셋_대기()
        if user_value(key='Phase_5_Interect_01', value=0):
            return 대기()


class 리셋_대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시작()
        if user_value(key='Phase_5_Interect_01', value=0):
            return 대기()


