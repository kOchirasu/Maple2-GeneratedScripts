""" trigger/52000160_qd/52000160.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002742], questStates=[3]):
            return 떠난다_01()
        if quest_user_detected(boxIds=[2001], questIds=[40002743], questStates=[3]):
            return 프론티아재단으로_01()
        if user_detected(boxIds=[2001], jobCode=0):
            return 전직컷씬01()


class 전직컷씬01(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChange_Assassin.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 다크윈드도착_01()
        if wait_tick(waitTick=8000):
            return 다크윈드도착_01()


class 다크윈드도착_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 다크윈드도착_02()


class 다크윈드도착_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 다크윈드도착_03()


class 다크윈드도착_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 다크윈드도착_04()


class 다크윈드도착_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 다크윈드도착_05()


class 다크윈드도착_05(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 다크윈드도착_06()


class 다크윈드도착_06(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 다크윈드도착_07()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 다크윈드도착_07()


class 다크윈드도착_07(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전직한다()


class 전직한다(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002742], questStates=[2]):
            return 전직이펙트_01()


class 전직이펙트_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전직이펙트_02()


class 전직이펙트_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 떠난다_01()


class 떠난다_01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002743], questStates=[3]):
            return 프론티아재단으로_01()


class 프론티아재단으로_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 프론티아재단으로_02()


class 프론티아재단으로_02(state.State):
    def on_enter(self):
        move_user(mapId=52000186, portalId=1)


