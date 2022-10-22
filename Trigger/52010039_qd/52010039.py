""" trigger/52010039_qd/52010039.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 영상재생_01()


class 영상재생_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='common\SkyFortress_Intro.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return start()
        if wait_tick(waitTick=170000):
            return start()


class start(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출종료02()


class 연출종료01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출종료02()


class 연출종료02(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 연출종료03()


class 연출종료03(state.State):
    def on_enter(self):
        set_sound(triggerId=9010, arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 스카이포트리스전경씬03()


class 스카이포트리스전경씬03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        show_caption(type='VerticalCaption', title='$52010039_QD__52010039__8$', desc='$52010039_QD__52010039__9$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)
        select_camera_path(pathIds=[1002,1003], returnView=False)
        set_scene_skip(state=Skip_1, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 스카이포트리스전경씬04()


class 스카이포트리스전경씬04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 스카이포트리스전경씬04_1()


class 스카이포트리스전경씬04_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit01()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit01()


class Quit01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        add_balloon_talk(spawnId=0, msg='$52010039_QD__52010039__10$', duration=6000, delayTick=1000)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 종료()


class 종료(state.State):
    pass


