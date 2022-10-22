""" trigger/99999949/04_camerareset.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9031]):
            return Guide()


class Guide(state.State):
    def on_enter(self):
        debug_string(string='4번 영역에 들어가면 CameraReset 트리거가 발동됩니다.')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9030]):
            return CameraReady()


class CameraReady(state.State):
    def on_enter(self):
        debug_string(string='SetOnetimeEffect 1초 후에 시작됩니다.')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraWalk01()


class CameraWalk01(state.State):
    def on_enter(self):
        debug_string(string='600번 카메라 선택')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=603, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraWalk03()


class CameraWalk03(state.State):
    def on_enter(self):
        debug_string(string='602번 카메라 선택')
        select_camera(triggerId=604, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraReset()


class CameraReset(state.State):
    def on_enter(self):
        debug_string(string='모든 카메라 리셋')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=604, enable=False) # action name="카메라리셋" interpolationTime="3.0"/

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        debug_string(string='5초 후에 트리거가 리셋됩니다. 4번 영역 밖으로 나가세요.')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait()


