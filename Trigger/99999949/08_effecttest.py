""" trigger/99999949/08_effecttest.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return Guide()


class Guide(state.State):
    def on_enter(self):
        debug_string(string='8번 영역에 들어가면 EffectTest 트리거가 발동됩니다.')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return CameraReady()


class CameraReady(state.State):
    def on_enter(self):
        debug_string(string='EffectTest 2초 후에 시작됩니다.')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 이펙트출력01()


class 이펙트출력01(state.State):
    def on_enter(self):
        debug_string(string='EffectTest 발동')
        set_effect(triggerIds=[9101,9102,9103,9104,9105,9106,9107,9108,9109,9110], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        debug_string(string='5초 후에 트리거가 리셋됩니다. 8번 영역 밖으로 나가세요.')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait()


