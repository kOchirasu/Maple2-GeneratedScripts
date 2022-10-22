""" trigger/52000199_qd/52000199_2.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003448], questStates=[2]):
            return CameraEffect01()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_user(mapId=52000199, portalId=5001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000199_QD__52000199_2__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return CameraEffect02_2()


class CameraEffect02_2(state.State):
    def on_enter(self):
        set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'], visible=False)
        add_buff(boxIds=[2001], skillId=99910403, level=1, arg4=False, arg5=True) # 다크로드 변신
        add_buff(boxIds=[2001], skillId=99910403, level=1, arg4=False, arg5=False) # 다크로드 변신

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


