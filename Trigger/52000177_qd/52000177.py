""" trigger/52000177_qd/52000177.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401], arg2=False)
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChange_ranger.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=8000):
            return 영상재생_end()


class 영상재생_end(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2001], visible=False)
        set_cinematic_ui(type=9, script='$52000177_QD__52000177__0$', arg3=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 영상재생_end02()


class 영상재생_end02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 전경씬01()


class 전경씬01(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_pc_emotion_loop(sequenceName='Sword_Attack_Idle_A', duration=10000, arg3=True)
        select_camera_path(pathIds=[4000,4001], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return 전경씬02()


class 전경씬02(state.State):
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
        show_guide_summary(entityId=52001771, textId=52001771, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002364], questStates=[3]):
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
        if wait_tick(waitTick=5000):
            return Quit03()


#  ########################전원 퇴장########################
class Quit03(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002366], questStates=[3]):
            return 전원퇴장01()


class 전원퇴장01(state.State):
    def on_enter(self):
        set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_mesh(triggerIds=[2001], visible=True)
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=11000)
        destroy_monster(spawnIds=[401])
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 전원퇴장02()


class 전원퇴장02(state.State):
    def on_enter(self):
        set_onetime_effect(id=10, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 전원퇴장03()


class 전원퇴장03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[402], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002368], questStates=[3]):
            return 프론티아재단으로01()


#  ########################퀘스트 종료########################
class 프론티아재단으로01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 프론티아재단으로02()


class 프론티아재단으로02(state.State):
    def on_enter(self):
        move_user(mapId=52000186, portalId=1)


