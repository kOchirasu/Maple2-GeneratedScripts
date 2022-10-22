""" trigger/52000162_qd/52000162.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001], jobCode=0):
            return wait_01_02()


# 컷씬
class wait_01_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        move_user(mapId=52000162, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wait_02()


class wait_02(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChangeStory.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 리스항구전경_01()
        if wait_tick(waitTick=85000):
            return 리스항구전경_01()


class 리스항구전경_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 리스항구전경_02()


class 리스항구전경_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004,4003], returnView=False)
        show_caption(type='VerticalCaption', title='$52000162_QD__52000162__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
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
        create_monster(spawnIds=[102], arg2=False)
        show_guide_summary(entityId=25201621, textId=25201621, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002744], questStates=[3]):
            return 리린등장_01()


class 리린등장_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 리린등장_02()


class 리린등장_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[101], arg2=False)
        select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 리린등장_03()


class 리린등장_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 리린등장_04()


class 리린등장_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_3001')
        set_scene_skip(state=Skip_2, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 정리2_01()


class 정리2_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정리2_02()


class 정리2_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 정리2_03()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정리2_03()


class 정리2_03(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002745], questStates=[3]):
            return 리엔으로_01()


class 리엔으로_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 리엔으로_02()


class 리엔으로_02(state.State):
    def on_enter(self):
        move_user(mapId=52000161, portalId=1)


