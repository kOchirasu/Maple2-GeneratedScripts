""" trigger/52000036_qd/darkmoonmovie.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return CameraEffect01()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera(triggerId=1000, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect4()


class CameraEffect4(state.State):
    def on_enter(self):
        select_camera(triggerId=1001, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return CameraEffect5()


class CameraEffect5(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        move_user(mapId=99999890, portalId=0)


