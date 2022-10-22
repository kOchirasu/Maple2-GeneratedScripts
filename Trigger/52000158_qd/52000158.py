""" trigger/52000158_qd/52000158.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002736], questStates=[3]):
            return 돌아왔다준비_01()
        if user_detected(boxIds=[2001], jobCode=0):
            return wait_01_1()


class wait_01_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        move_user(mapId=52000158, portalId=6001)

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

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 커닝시티전경_02()


class 커닝시티전경_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002], returnView=False)
        show_caption(type='VerticalCaption', title='$52000158_QD__52000158__0$', desc='$52000158_QD__52000158__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 어쌔신_01()


class 어쌔신_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 암전()


class 암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return UI초기화()


class UI초기화(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 밝아짐()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 밝아짐()


class 밝아짐(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        reset_camera(interpolationTime=0)
        create_monster(spawnIds=[101], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002733], questStates=[3]):
            return 이동_01()
        if quest_user_detected(boxIds=[2001], questIds=[40002732], questStates=[2]):
            return 퀘스트가이드()


class 퀘스트가이드(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25201581, textId=25201581, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002734], questStates=[2]):
            return 이동_01()


class 이동_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 이동_02()


class 이동_02(state.State):
    def on_enter(self):
        move_user(mapId=52000159, portalId=1)


class 돌아왔다준비_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 돌아왔다_01()


class 돌아왔다_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 돌아왔다_02()


class 돌아왔다_02(state.State):
    def on_enter(self):
        move_user(mapId=52000158, portalId=6001)
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002741], questStates=[2]):
            return 이동2_01()


class 이동2_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 이동2_02()


class 이동2_02(state.State):
    def on_enter(self):
        move_user(mapId=52000160, portalId=1)


