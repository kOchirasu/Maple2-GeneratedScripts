""" trigger/52000183_qd/52000183.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_monster(spawnIds=[500], arg2=False)
        create_monster(spawnIds=[501], arg2=False)
        create_monster(spawnIds=[502], arg2=False)
        create_monster(spawnIds=[503], arg2=False)
        create_monster(spawnIds=[504], arg2=False)
        create_monster(spawnIds=[505], arg2=False)
        create_monster(spawnIds=[506], arg2=False)
        create_monster(spawnIds=[507], arg2=False)
        create_monster(spawnIds=[508], arg2=False)
        create_monster(spawnIds=[509], arg2=False)
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChange_priest.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 전경씬01()
        if wait_tick(waitTick=8000):
            return 전경씬01()


class 전경씬01(state.State):
    def on_enter(self):
        move_user(mapId=52000183, portalId=80)
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        select_camera_path(pathIds=[4000,4001,4002], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전경씬02_b()


class 전경씬02_b(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Priest_HeavensPray3_A'])
        set_npc_emotion_loop(spawnId=500, sequenceName='Bore_A', duration=8000)
        set_npc_emotion_loop(spawnId=501, sequenceName='Idle_A', duration=8000)
        set_npc_emotion_loop(spawnId=502, sequenceName='Idle_A', duration=8000)
        set_npc_emotion_loop(spawnId=503, sequenceName='Bore_A', duration=8000)
        set_npc_emotion_loop(spawnId=504, sequenceName='Idle_A', duration=8000)
        set_npc_emotion_loop(spawnId=505, sequenceName='Bore_A', duration=8000)
        set_npc_emotion_loop(spawnId=506, sequenceName='Idle_A', duration=8000)
        set_npc_emotion_loop(spawnId=507, sequenceName='Bore_A', duration=8000)

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
        move_npc(spawnId=502, patrolName='MS2PatrolData_502')
        move_npc(spawnId=503, patrolName='MS2PatrolData_503')
        move_npc(spawnId=505, patrolName='MS2PatrolData_505')
        move_npc(spawnId=506, patrolName='MS2PatrolData_506')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        show_guide_summary(entityId=52001831, textId=52001831, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002341], questStates=[3]):
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
        if quest_user_detected(boxIds=[9001], questIds=[20002342], questStates=[3]):
            return 가브란트퇴장01()


#  ########################전원 퇴장########################
class 가브란트퇴장01(state.State):
    def on_enter(self):
        move_npc(spawnId=509, patrolName='MS2PatrolData_gabExit')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9002, spawnIds=[509]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[509])

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002343], questStates=[3]):
            return 전원퇴장01()


class 전원퇴장01(state.State):
    def on_enter(self):
        set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전원퇴장01_b()


class 전원퇴장01_b(state.State):
    def on_enter(self):
        move_user(mapId=52000183, portalId=81)
        destroy_monster(spawnIds=[500])
        destroy_monster(spawnIds=[501])
        destroy_monster(spawnIds=[502])
        destroy_monster(spawnIds=[502])
        destroy_monster(spawnIds=[503])
        destroy_monster(spawnIds=[504])
        destroy_monster(spawnIds=[505])
        destroy_monster(spawnIds=[506])
        destroy_monster(spawnIds=[507])
        destroy_monster(spawnIds=[508])
        destroy_monster(spawnIds=[509])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전원퇴장02()


class 전원퇴장02(state.State):
    def on_enter(self):
        set_onetime_effect(id=10, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        show_guide_summary(entityId=52001832, textId=52001832, duration=10000)
        create_monster(spawnIds=[510], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002345], questStates=[3]):
            return 프론티아재단으로01()


#  ########################퀘스트 종료########################
class 프론티아재단으로01(state.State):
    def on_enter(self):
        set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 프론티아재단으로02()


class 프론티아재단으로02(state.State):
    def on_enter(self):
        move_user(mapId=52000186, portalId=1)


