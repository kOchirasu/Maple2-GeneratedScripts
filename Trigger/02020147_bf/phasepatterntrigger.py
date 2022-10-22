""" trigger/02020147_bf/phasepatterntrigger.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_user_value(key='PhaseSumTotal', value=0) # PhaseSumTotal 변수 0으로 초기 세팅
        set_user_value(key='PhasePatternTrigger', value=0) # PhasePatternTrigger 변수 0으로 초기 세팅

    def on_tick(self) -> state.State:
        if count_users(boxId=601, boxId=1):
            return 보스3마리_페이즈전환계산()


class 보스3마리_페이즈전환계산(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='PhaseSumTotal', value=3, operator='GreaterEqual'):
            return 보스3마리_페이즈전환실행_2페이즈()


class 보스3마리_페이즈전환실행_2페이즈(state.State):
    def on_enter(self):
        set_ai_extra_data(key='PhasePatternTrigger', value=2) # PhasePatternTrigger = 2 신호를 보스 3마리한테 보내서 2페이즈로 전환하도록 함

    def on_tick(self) -> state.State:
        if user_value(key='PhaseSumTotal', value=6, operator='GreaterEqual'):
            return 보스3마리_페이즈전환실행_3페이즈()


class 보스3마리_페이즈전환실행_3페이즈(state.State):
    def on_enter(self):
        set_ai_extra_data(key='PhasePatternTrigger', value=3) # PhasePatternTrigger = 3 신호를 보스 3마리한테 보내서 3페이즈로 전환하도록 함

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 종료()


class 종료(state.State):
    pass


