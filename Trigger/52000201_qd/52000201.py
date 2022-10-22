""" trigger/52000201_qd/52000201.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003429], questStates=[2]):
            return CameraEffect01()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera_path(pathIds=[4001], returnView=False)
        move_user(mapId=52000201, portalId=5001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect04()


class CameraEffect04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return CameraEffect05()


class CameraEffect05(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect07()


class CameraEffect07(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


