""" trigger/52000152_qd/52000152.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=1000, visible=False, enabled=False, minimapVisible=False)
        move_user(mapId=52000152, portalId=1010)
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
            return 묘지전경씬01()
        if wait_tick(waitTick=85000):
            return 묘지전경씬01()


class 묘지전경씬01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 묘지전경씬02_1()


class 묘지전경씬02_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_user_path(patrolName='MS2PatrolData_PC_Walk')
        select_camera_path(pathIds=[4000,4001], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 묘지전경씬02()


class 묘지전경씬02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4003,4004,4005], returnView=False)
        show_caption(type='VerticalCaption', title='$52000152_QD__52000152__0$', desc='$52000152_QD__52000152__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 묘지전경씬03()


class 묘지전경씬03(state.State):
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
        add_balloon_talk(spawnId=0, msg='$52000152_QD__52000152__2$', duration=6000, delayTick=1000)
        show_guide_summary(entityId=25201521, textId=25201521, duration=10000)
        create_monster(spawnIds=[2000], arg2=False) # 조디의무덤

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002328], questStates=[3]):
            return 제니아등장01()


#  ########################씬2 케이틀린 등장########################
class 제니아등장01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False) # 제니아
        move_npc(spawnId=2001, patrolName='MS2PatrolData_xeniaMove')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002332], questStates=[3]):
            return 수련장이동01()


class 수련장이동01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 수련장이동02()


class 수련장이동02(state.State):
    def on_enter(self):
        move_user(mapId=52000153, portalId=1)


