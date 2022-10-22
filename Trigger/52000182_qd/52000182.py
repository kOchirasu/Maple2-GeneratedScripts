""" trigger/52000182_qd/52000182.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=1000, visible=False, enabled=False, minimapVisible=False)
        move_user(mapId=52000182, portalId=1010)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChangeStory.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 병원전경씬01()
        if wait_tick(waitTick=85000):
            return 병원전경씬01()


class 병원전경씬01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        create_monster(spawnIds=[400], arg2=False)
        create_monster(spawnIds=[401], arg2=False)
        create_monster(spawnIds=[402], arg2=False)
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 병원전경씬02_1()


class 병원전경씬02_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_user_path(patrolName='MS2PatrolData_PC_Walk')
        select_camera_path(pathIds=[4000,4001,4002,4003], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 병원전경씬02()


class 병원전경씬02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004,4005,4006,4007], returnView=False)
        show_caption(type='VerticalCaption', title='$52000182_QD__52000182__0$', desc='$52000182_QD__52000182__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 병원전경씬03()


class 병원전경씬03(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit01()


class Quit01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        add_balloon_talk(spawnId=0, msg='$52000182_QD__52000182__2$', duration=6000, delayTick=1000)
        show_guide_summary(entityId=52001821, textId=52001821, duration=10000)
        create_monster(spawnIds=[2000], arg2=False) # 조디의무덤

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002337], questStates=[3]):
            return 치유마법전개01()


#  ########################치유 마법 전개########################
class 치유마법전개01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 치유마법전개02()


class 치유마법전개02(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 치유마법전개03()


class 치유마법전개03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002340], questStates=[3]):
            return 수련장이동01()


class 수련장이동01(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 수련장이동02()


class 수련장이동02(state.State):
    def on_enter(self):
        move_user(mapId=52000183, portalId=1)


