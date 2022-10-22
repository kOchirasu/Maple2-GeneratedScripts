""" trigger/52000174_qd/52000174.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002768], questStates=[2]):
            return 이도공간으로_01()
        if quest_user_detected(boxIds=[2001], questIds=[40002776], questStates=[3]):
            return 프론티아재단으로_01()
        if quest_user_detected(boxIds=[2001], questIds=[40002770], questStates=[3]):
            return 전직컷씬01()
        if user_detected(boxIds=[2001]):
            return wait_01_02()


class wait_01_02(state.State):
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
        move_user(mapId=52000174, portalId=1)
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 숙소도착_01()
        if wait_tick(waitTick=85000):
            return 숙소도착_01()


class 숙소도착_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 숙소도착_02()


class 숙소도착_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002], returnView=False)
        show_caption(type='VerticalCaption', title='$52000174_QD__52000174__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)
        move_user_path(patrolName='MS2PatrolData_3003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 숙소도착_03()


class 숙소도착_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 숙소도착_04()


class 숙소도착_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 숙소도착_05()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 숙소도착_05()


class 숙소도착_05(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=25201741, textId=25201741, duration=3000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002768], questStates=[2]):
            return 이도공간으로_01()


class 이도공간으로_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 이도공간으로_02()


class 이도공간으로_02(state.State):
    def on_enter(self):
        move_user(mapId=52000173, portalId=1)


class 전직컷씬01(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChange_soul.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 깨어났다_01()
        if wait_tick(waitTick=8000):
            return 깨어났다_01()


class 깨어났다_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 깨어났다_02()


class 깨어났다_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        move_user(mapId=52000174, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 깨어났다_03()


class 깨어났다_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_2, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 깨어났다_04()


class 깨어났다_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003,4004], returnView=False)
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 깨어났다_05()


class 깨어났다_05(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 깨어났다_06()


class 깨어났다_06(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 깨어났다_07()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 깨어났다_07()


class 깨어났다_07(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002771], questStates=[3]):
            return 전직이펙트_01()


class 전직이펙트_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전직이펙트_02()


class 전직이펙트_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 비젼생성_01()


class 비젼생성_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002775], questStates=[3]):
            return 떠나기전_04_01()


class 떠나기전_04_01(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_3002')
        move_npc(spawnId=104, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 떠나기전_05()


class 떠나기전_05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[104])

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002776], questStates=[3]):
            return 프론티아재단으로_01()


class 프론티아재단으로_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 프론티아재단으로_02()


class 프론티아재단으로_02(state.State):
    def on_enter(self):
        move_user(mapId=52000186, portalId=1)


