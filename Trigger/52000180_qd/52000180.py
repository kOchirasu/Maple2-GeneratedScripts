""" trigger/52000180_qd/52000180.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001], jobCode=0):
            return 전직컷씬01()


class 전직컷씬01(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChange_wizard.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return wait_01_02()
        if wait_tick(waitTick=8000):
            return wait_01_02()


class wait_01_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[101], arg2=False)
        move_user(mapId=52000180, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 숲전경_01()


class 숲전경_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 숲전경_02()


class 숲전경_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정리_01()


class 정리_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정리_02()


class 정리_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 정리_03()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정리_03()


class 정리_03(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002760], questStates=[2]):
            return 전직이펙트_01()
        if quest_user_detected(boxIds=[2001], questIds=[40002760], questStates=[3]):
            return 이동_01()


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
            return 이동하자()


class 이동하자(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002760], questStates=[3]):
            return 이동_01()


class 이동_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 이동_02()


class 이동_02(state.State):
    def on_enter(self):
        move_user(mapId=52000181, portalId=1)


