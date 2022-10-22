""" trigger/52000164_qd/52000164.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=1000, visible=False, enabled=False, minimapVisible=False)
        move_user(mapId=52000164, portalId=1010)
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
            return 연구실전경씬01()
        if wait_tick(waitTick=85000):
            return 연구실전경씬01()


class 연구실전경씬01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')
        create_monster(spawnIds=[400], arg2=False) # 아이샤
        create_monster(spawnIds=[401], arg2=False) # 아이샤
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연구실전경씬02_1()


class 연구실전경씬02_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연구실전경씬02()


class 연구실전경씬02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4000,4001,4002], returnView=False)
        move_npc(spawnId=400, patrolName='MS2PatrolData_isha')
        move_user_path(patrolName='MS2PatrolData_pc')
        show_caption(type='VerticalCaption', title='$52000164_QD__52000164__0$', desc='$52000164_QD__52000164__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연구실전경씬03()


class 연구실전경씬03(state.State):
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
        show_guide_summary(entityId=52001641, textId=52001641, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002348], questStates=[3]):
            return 아이샤이동01()


class 아이샤이동01(state.State):
    def on_enter(self):
        move_npc(spawnId=400, patrolName='MS2PatrolData_isha2')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002354], questStates=[3]):
            return 본격연구시작01()


#  ########################씬2 케이틀린 등장########################
class 본격연구시작01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 본격연구시작02()


class 본격연구시작02(state.State):
    def on_enter(self):
        move_user(mapId=52000165, portalId=1)


