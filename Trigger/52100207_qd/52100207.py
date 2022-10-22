""" trigger/52100207_qd/52100207.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003190], questStates=[2]):
            return wait_01_02()


class wait_01_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4001], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 요랑의방_01()


class 요랑의방_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 요랑의방_02()


class 요랑의방_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52100207_QD__52100207__0$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 요랑의방_04()


class 요랑의방_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52100207_QD__52100207__1$', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 요랑의방_05()


class 요랑의방_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52100207_QD__52100207__2$', duration=1500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 요랑의방_06()


class 요랑의방_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52100207_QD__52100207__3$', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정리_01()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정리_01()


class 정리_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 정리_02()


class 정리_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


