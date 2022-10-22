""" trigger/02020301_bf/3000037_phase_2_interect_07.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Phase_2_Interect_07', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[706], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[706]):
            return 재생성()
        if user_value(key='Phase_2_Interect_07', value=0):
            return 대기()


class 재생성(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 시작()
        if user_value(key='Phase_2_Interect_07', value=0):
            return 대기()


