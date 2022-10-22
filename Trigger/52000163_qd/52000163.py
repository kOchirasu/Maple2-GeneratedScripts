""" trigger/52000163_qd/52000163.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001], jobCode=0):
            return 전직컷씬01()


# 컷씬
class 전직컷씬01(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChange_berserker.swf', movieId=1)
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 리엔원경_01_03()
        if wait_tick(waitTick=8000):
            return 리엔원경_01_03()


class 리엔원경_01_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003,4004], returnView=False)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 리엔원경_02()


class 리엔원경_02(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000163_QD__52000163__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 정리2_01()


class 정리2_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 정리2_02()


class 정리2_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 정리2_03()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정리2_03()


class 정리2_03(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=52000163, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전직준비()


class 전직준비(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002750], questStates=[3]):
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
            return 떠나기전준비()


class 떠나기전준비(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002753], questStates=[3]):
            return 프론티아재단으로_01()


class 프론티아재단으로_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 프론티아재단으로_02()


class 프론티아재단으로_02(state.State):
    def on_enter(self):
        move_user(mapId=52000186, portalId=1)


