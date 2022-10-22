""" trigger/52000167_qd/52000167.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=1000, visible=False, enabled=False, minimapVisible=False)
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
        set_effect(triggerIds=[700], visible=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 묘지전경씬02_1()


class 묘지전경씬02_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_user_path(patrolName='MS2PatrolData_pc')
        select_camera_path(pathIds=[4000,4001,4002,4003], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 묘지전경씬02()


class 묘지전경씬02(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000167_QD__52000167__0$', desc='$52000167_QD__52000167__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 묘지전경씬03()


class 묘지전경씬03(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
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
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        add_balloon_talk(spawnId=0, msg='$52000167_QD__52000167__2$', duration=6000, delayTick=1000)
        show_guide_summary(entityId=52001671, textId=52001671, duration=10000)
        create_monster(spawnIds=[400], arg2=False) # 조디의무덤

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002369], questStates=[3]):
            return 홀슈타트등장00()


#  ########################씬2 케이틀린 등장########################
class 홀슈타트등장00(state.State):
    def on_enter(self):
        set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[401], arg2=False)
        create_monster(spawnIds=[402], arg2=False)
        create_monster(spawnIds=[403], arg2=False)
        create_monster(spawnIds=[404], arg2=False)
        create_monster(spawnIds=[405], arg2=False)
        create_monster(spawnIds=[406], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 홀슈타트등장01()


class 홀슈타트등장01(state.State):
    def on_enter(self):
        set_onetime_effect(id=20, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[5000,5001,5002,5003,5004], returnView=False)
        move_npc(spawnId=402, patrolName='MS2PatrolData_402_hol')
        move_npc(spawnId=403, patrolName='MS2PatrolData_403')
        move_npc(spawnId=404, patrolName='MS2PatrolData_404')
        move_npc(spawnId=405, patrolName='MS2PatrolData_405')
        move_npc(spawnId=406, patrolName='MS2PatrolData_406')
        move_user_path(patrolName='MS2PatrolData_pc_move')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 홀슈타트등장02_c()


class 홀슈타트등장02_c(state.State):
    def on_enter(self):
        set_effect(triggerIds=[700], visible=True)
        set_time_scale(enable=True, startScale=1, endScale=0.3, duration=3.5, interpolator=2) # 2초간 느려지기 시작
        add_balloon_talk(spawnId=0, msg='$52000167_QD__52000167__3$', duration=6000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 홀슈타트등장02()


class 홀슈타트등장02(state.State):
    def on_enter(self):
        set_onetime_effect(id=40, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 홀슈타트등장03()


class 홀슈타트등장03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=52001672, textId=52001672, duration=10000)
        set_onetime_effect(id=40, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002370], questStates=[3]):
            return 홀슈타트등장04()


class 홀슈타트등장04(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=402, sequenceName='Attack_Idle_A', duration=800000)
        set_npc_emotion_loop(spawnId=403, sequenceName='Attack_Idle_A', duration=800000)
        set_npc_emotion_loop(spawnId=404, sequenceName='Attack_Idle_A', duration=800000)
        set_npc_emotion_loop(spawnId=405, sequenceName='Attack_Idle_A', duration=800000)
        set_npc_emotion_loop(spawnId=406, sequenceName='Attack_Idle_A', duration=800000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002371], questStates=[3]):
            return 수련장이동01()


class 수련장이동01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=100000, arg3=True)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 수련장이동02()


class 수련장이동02(state.State):
    def on_enter(self):
        move_user(mapId=52000168, portalId=80)


