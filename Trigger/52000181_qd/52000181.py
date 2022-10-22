""" trigger/52000181_qd/52000181.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001], jobCode=0):
            return wait_01_02()


class wait_01_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wait_01_03()


class wait_01_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        move_user(mapId=520001781, portalId=1)
        create_monster(spawnIds=[101], arg2=False)
        select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연구실도착_01()


class 연구실도착_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연구실도착_02()


class 연구실도착_02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_3001')
        move_user_path(patrolName='MS2PatrolData_3002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 정리_01()


class 정리_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 정리_02()


class 정리_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
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
        destroy_monster(spawnIds=[101], arg2=False)
        move_user(mapId=52000181, portalId=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002765], questStates=[3]):
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


