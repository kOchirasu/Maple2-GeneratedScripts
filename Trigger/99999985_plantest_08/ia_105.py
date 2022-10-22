""" trigger/99999985_plantest_08/ia_105.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        debug_string(value='환경음 테스트 트리거 입니다. 환경음을 켭니다. (HeavyRain)')
        set_sound(triggerId=10001, arg2=True)
        weather(weatherType='HeavyRain')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_enter(self):
        debug_string(value='환경음이 꺼집니다.')
        set_sound(triggerId=10001, arg2=False)
        weather(weatherType='None')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 시작대기중()


