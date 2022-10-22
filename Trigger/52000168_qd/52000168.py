""" trigger/52000168_qd/52000168.xml """
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
        create_monster(spawnIds=[401], arg2=False) # 바사라첸
        create_monster(spawnIds=[402], arg2=False) # 바사라첸
        create_monster(spawnIds=[403], arg2=False) # 바사라첸
        create_monster(spawnIds=[404], arg2=False) # 바사라첸
        create_monster(spawnIds=[405], arg2=False) # 바사라첸
        create_monster(spawnIds=[406], arg2=False) # 바사라첸
        move_user(mapId=52000168, portalId=80)
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChange_RBlader.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 전경씬01()
        if wait_tick(waitTick=8000):
            return 전경씬01()


class 전경씬01(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_pc_emotion_loop(sequenceName='Push_A', duration=10000, arg3=True)
        set_npc_emotion_loop(spawnId=402, sequenceName='Attack_Idle_A', duration=1000000)
        set_npc_emotion_loop(spawnId=403, sequenceName='Dead_A', duration=800000)
        set_npc_emotion_loop(spawnId=404, sequenceName='Dead_A', duration=800000)
        set_npc_emotion_loop(spawnId=405, sequenceName='Dead_A', duration=800000)
        set_npc_emotion_loop(spawnId=406, sequenceName='Dead_A', duration=800000)
        select_camera_path(pathIds=[4000,4001,4003], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
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
        show_guide_summary(entityId=52001681, textId=52001681, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002373], questStates=[3]):
            return 전직이펙트_01()


class 전직이펙트_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전직이펙트_02()


class 전직이펙트_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[402])
        destroy_monster(spawnIds=[403])
        destroy_monster(spawnIds=[404])
        destroy_monster(spawnIds=[405])
        destroy_monster(spawnIds=[406])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전직이펙트_03()


class 전직이펙트_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit03()


#  ########################퀘스트 종료########################
class Quit03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[402])
        destroy_monster(spawnIds=[403])
        destroy_monster(spawnIds=[404])
        destroy_monster(spawnIds=[405])
        destroy_monster(spawnIds=[406])
        create_monster(spawnIds=[500], arg2=False)
        create_monster(spawnIds=[501], arg2=False)
        create_monster(spawnIds=[502], arg2=False)
        move_npc(spawnId=500, patrolName='MS2PatrolData_500')
        move_npc(spawnId=501, patrolName='MS2PatrolData_501')
        move_npc(spawnId=502, patrolName='MS2PatrolData_502')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002374], questStates=[3]):
            return 칼리브요새로01()


class 칼리브요새로01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 칼리브요새로02()


class 칼리브요새로02(state.State):
    def on_enter(self):
        move_user(mapId=52000169, portalId=1)


