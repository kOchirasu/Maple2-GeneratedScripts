""" trigger/52000156_qd/52000156.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001]):
            return wait_01_1()


class wait_01_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wait_02()


class wait_02(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChangeStory.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 커닝시티전경_01()
        if wait_tick(waitTick=85000):
            return 커닝시티전경_01()


class 커닝시티전경_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')
        select_camera_path(pathIds=[4001,4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 커닝시티전경_02()


class 커닝시티전경_02(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000156_QD__52000156__0$', desc='$52000156_QD__52000156__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 암전()


class 암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return UI초기화()


class UI초기화(state.State):
    def on_enter(self):
        move_user(mapId=52000156, portalId=6003)
        create_monster(spawnIds=[101], arg2=False)
        select_camera_path(pathIds=[4003,4004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 밝아짐()


class 밝아짐(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        move_user_path(patrolName='MS2PatrolData_3001')
        # Missing State: Skip_2
        set_scene_skip(arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 조나단만남()


class 조나단만남(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 조나단만남_2()


class 조나단만남_2(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 조나단만남_3()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        move_user(mapId=52000156, portalId=6003)
        destroy_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[101], arg2=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 조나단만남_3()


class 조나단만남_3(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


