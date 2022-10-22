""" trigger/02020301_bf/300003_phase_2.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='AI_Phase', value=2):
            return 패이즈_2_시작()


class 패이즈_2_시작(state.State):
    def on_enter(self):
        set_user_value(key='AI_Phase', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아르케온_탈것_생성()


class 아르케온_탈것_생성(state.State):
    def on_enter(self):
        set_user_value(triggerId=3000031, key='Phase_2_Interect_01', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 쫄몹등장()


class 쫄몹등장(state.State):
    def on_enter(self):
        set_user_value(triggerId=3000032, key='Phase_2_Interect_02', value=1)
        set_user_value(triggerId=3000033, key='Phase_2_Interect_03', value=1)
        set_user_value(triggerId=3000034, key='Phase_2_Interect_04', value=1)
        set_user_value(triggerId=3000035, key='Phase_2_Interect_05', value=1)
        set_user_value(triggerId=3000036, key='Phase_2_Interect_06', value=1)
        set_user_value(triggerId=3000037, key='Phase_2_Interect_07', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


