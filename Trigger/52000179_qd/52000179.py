""" trigger/52000179_qd/52000179.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001], jobCode=0):
            return wait_01_02()


class wait_01_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        move_user(mapId=52000179, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wait_02()


class wait_02(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChangeStory.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 숲전경_01()
        if wait_tick(waitTick=85000):
            return 숲전경_01()


class 숲전경_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')
        select_camera_path(pathIds=[4001,4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 숲전경_02()


class 숲전경_02(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000179_QD__52000179__0$', desc='$52000179_QD__52000179__2$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

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

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002757], questStates=[2]):
            return 퀘스트가이드_01()
        if quest_user_detected(boxIds=[2001], questIds=[40002757], questStates=[3]):
            return 케이틀린걱정()


class 퀘스트가이드_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25201791, textId=25201791, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002757], questStates=[3]):
            return 케이틀린걱정()


class 케이틀린걱정(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_3001')
        add_balloon_talk(spawnId=101, msg='$52000179_QD__52000179__1$', duration=3000, delayTick=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002758], questStates=[3]):
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
        move_user(mapId=52000180, portalId=1)


