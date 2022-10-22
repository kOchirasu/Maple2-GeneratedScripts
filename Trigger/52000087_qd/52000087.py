""" trigger/52000087_qd/52000087.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[22651], questIds=[10003370], questStates=[2]):
            return 보고시작준비_01()


#  에레브여제에게 보고 
class 보고시작준비_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        move_user(mapId=52000087, portalId=6001)
        select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 보고시작준비_02()


class 보고시작준비_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4002], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3001')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return 보고시작준비_03()


class 보고시작준비_03(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Talk_A', duration=5000)
        select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 보고시작준비_04()


class 보고시작준비_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 보고시작_01()


class 보고시작_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087__0$')
        move_user(mapId=52000087, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='Kritias_EpicCutScene_second_01.swf', movieId=1)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return Quit()
        if wait_tick(waitTick=35000):
            return Quit()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52000087, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)


