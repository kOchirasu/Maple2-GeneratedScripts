""" trigger/52000161_qd/52000161.xml """
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
        create_monster(spawnIds=[101], arg2=False)
        move_user(mapId=52000161, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 리엔전경_01()


class 리엔전경_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 리엔전경_02()


class 리엔전경_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002], returnView=False)
        show_caption(type='VerticalCaption', title='$52000161_QD__52000161__0$', desc='$52000161_QD__52000161__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)
        move_npc(spawnId=101, patrolName='MS2PatrolData_3001')
        move_user_path(patrolName='MS2PatrolData_3002')

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
        destroy_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        move_user(mapId=52000161, portalId=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002750], questStates=[2]):
            return 전직하러()


class 전직하러(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전직하러_01()


class 전직하러_01(state.State):
    def on_enter(self):
        move_user(mapId=52000163, portalId=2)


