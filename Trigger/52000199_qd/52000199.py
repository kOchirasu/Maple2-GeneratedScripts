""" trigger/52000199_qd/52000199.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001], jobCode=0):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        move_user(mapId=52000199, portalId=5001)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003416], questStates=[2]):
            return CameraEffect01()
        if quest_user_detected(boxIds=[2001], questIds=[10003417], questStates=[1]):
            return Wait_02()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_3()


class CameraEffect03_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)
        show_caption(type='VerticalCaption', title='$52000199_QD__52000199__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return CameraEffect04()


class CameraEffect04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect05()


class CameraEffect05(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003417], questStates=[1]):
            return Wait_02()


class Wait_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='common\KiliansTruth.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 바깥으로()
        if wait_tick(waitTick=203000):
            return 바깥으로()


class 바깥으로(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        set_achievement(triggerId=2001, achieve='KiliansTruth')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 바깥으로_02()


class 바깥으로_02(state.State):
    def on_enter(self):
        move_user(mapId=2000146, portalId=12)


