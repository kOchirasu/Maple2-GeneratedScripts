""" trigger/52000101_qd/52000101.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_portal(portalId=1000, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5304], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5305], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5306], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5307], visible=False) # 목표 바닥 지점01 NPC
        set_effect(triggerIds=[5308], visible=False) # 목표 바닥 지점03 포탈
        set_effect(triggerIds=[5309], visible=False) # 화살표01 NPC
        set_effect(triggerIds=[5310], visible=False) # 경로 안내
        set_effect(triggerIds=[5311], visible=False) # 경로 안내
        set_effect(triggerIds=[5312], visible=False) # 경로 안내
        set_effect(triggerIds=[5313], visible=False) # 경로 안내
        set_effect(triggerIds=[5314], visible=False) # 경로 안내
        set_effect(triggerIds=[5315], visible=False) # 경로 안내
        set_effect(triggerIds=[5316], visible=False) # 경로 안내
        set_effect(triggerIds=[5317], visible=False) # 경로 안내
        set_effect(triggerIds=[5318], visible=False) # 경로 안내
        set_effect(triggerIds=[5319], visible=False) # 경로 안내
        set_effect(triggerIds=[5320], visible=False) # 경로 안내
        set_effect(triggerIds=[5321], visible=False) # 경로 안내
        set_effect(triggerIds=[5322], visible=False) # 경로 안내
        move_user(mapId=52000101, portalId=1010)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[4000]):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='common\JobIntro_Wizard.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 엘리니아전경씬01()
        if wait_tick(waitTick=62000):
            return 엘리니아전경씬01()


class 엘리니아전경씬01(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[1100,1101], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 엘리니아전경씬02()


class 엘리니아전경씬02(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000101_QD__52000101__0$', desc='$52000101_QD__52000101__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 엘리니아전경씬03()


class 엘리니아전경씬03(state.State):
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
        set_effect(triggerIds=[5304], visible=True) # 경로 안내
        set_effect(triggerIds=[5305], visible=True) # 경로 안내
        set_effect(triggerIds=[5306], visible=True) # 경로 안내
        set_effect(triggerIds=[5307], visible=True) # 경로 안내
        set_effect(triggerIds=[5308], visible=True) # 경로 안내
        set_effect(triggerIds=[5309], visible=True) # 경로 안내
        set_effect(triggerIds=[5310], visible=True) # 경로 안내
        set_effect(triggerIds=[5311], visible=True) # 경로 안내
        set_effect(triggerIds=[5312], visible=True) # 경로 안내
        set_effect(triggerIds=[5313], visible=True) # 경로 안내
        set_effect(triggerIds=[5314], visible=True) # 경로 안내
        set_effect(triggerIds=[5315], visible=True) # 경로 안내
        set_effect(triggerIds=[5316], visible=True) # 경로 안내
        set_effect(triggerIds=[5317], visible=True) # 경로 안내
        set_effect(triggerIds=[5318], visible=True) # 경로 안내
        set_effect(triggerIds=[5319], visible=True) # 경로 안내
        set_effect(triggerIds=[5320], visible=True) # 경로 안내
        set_effect(triggerIds=[5321], visible=True) # 경로 안내
        set_effect(triggerIds=[5322], visible=True) # 경로 안내
        add_balloon_talk(spawnId=0, msg='$52000101_QD__52000101__2$', duration=6000, delayTick=1000)
        show_guide_summary(entityId=25201011, textId=25201011, duration=10000)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[4001]):
            return 케이틀린등장씬01()


#  ########################씬2 케이틀린 등장########################
class 케이틀린등장씬01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[200], arg2=False) # 케이틀린

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 케이틀린등장씬02()


class 케이틀린등장씬02(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_2, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_npc(spawnId=200, patrolName='MS2PatrolData_caitCome')
        select_camera_path(pathIds=[1002,1003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 케이틀린등장씬03()


class 케이틀린등장씬03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1004,1005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 케이틀린등장씬04_b()


class 케이틀린등장씬04_b(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=200, sequenceName='Bore_B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 케이틀린등장씬04()


class 케이틀린등장씬04(state.State):
    def on_enter(self):
        show_caption(type='NameCaption', title='$52000101_QD__52000101__3$', desc='$52000101_QD__52000101__4$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=10000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 케이틀린등장씬04_1()


class 케이틀린등장씬04_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 케이틀린등장씬05()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        move_npc(spawnId=200, patrolName='MS2PatrolData_caitCome')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 케이틀린등장씬05()


class 케이틀린등장씬05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)
        set_effect(triggerIds=[5304], visible=False) # 경로 안내
        set_effect(triggerIds=[5305], visible=False) # 경로 안내
        set_effect(triggerIds=[5306], visible=False) # 경로 안내
        set_effect(triggerIds=[5307], visible=False) # 경로 안내
        set_effect(triggerIds=[5308], visible=False) # 경로 안내
        set_effect(triggerIds=[5309], visible=False) # 경로 안내
        set_effect(triggerIds=[5310], visible=False) # 경로 안내
        set_effect(triggerIds=[5311], visible=False) # 경로 안내
        set_effect(triggerIds=[5312], visible=False) # 경로 안내
        set_effect(triggerIds=[5313], visible=False) # 경로 안내
        set_effect(triggerIds=[5314], visible=False) # 경로 안내
        set_effect(triggerIds=[5315], visible=False) # 경로 안내
        set_effect(triggerIds=[5316], visible=False) # 경로 안내
        set_effect(triggerIds=[5317], visible=False) # 경로 안내
        set_effect(triggerIds=[5318], visible=False) # 경로 안내
        set_effect(triggerIds=[5319], visible=False) # 경로 안내
        set_effect(triggerIds=[5320], visible=False) # 경로 안내
        set_effect(triggerIds=[5321], visible=False) # 경로 안내
        set_effect(triggerIds=[5322], visible=False) # 경로 안내
        face_emotion(spawnId=200)
        show_guide_summary(entityId=25201012, textId=25201012, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[4001], questIds=[20002286], questStates=[3]):
            return 케이틀린화남01()
        if quest_user_detected(boxIds=[4001], questIds=[20002286], questStates=[2]):
            return 케이틀린화남01()


#  ########################씬3 케이틀린과 대화퀘스트 이후########################
class 케이틀린화남01(state.State):
    def on_enter(self):
        set_scene_skip(state=케이틀린화남06, arg2='exit')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000101, portalId=1011)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 케이틀린화남02()


class 케이틀린화남02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        add_cinematic_talk(npcId=0, msg='$52000101_QD__52000101__5$', duration=4000, align='right')
        select_camera_path(pathIds=[1006,1007], returnView=False)
        move_npc(spawnId=200, patrolName='MS2PatrolData_caitTurn') # 마드리아 이동
        move_user_path(patrolName='MS2PatrolData_PC_Run')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 케이틀린화남03()


class 케이틀린화남03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003146, msg='$52000101_QD__52000101__6$', duration=4000, align='right')
        set_onetime_effect(id=3000946, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000946.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 케이틀린화남04()


class 케이틀린화남04(state.State):
    def on_enter(self):
        face_emotion(spawnId=200, emotionName='UpSet')
        select_camera_path(pathIds=[1008,1009], returnView=False)
        add_cinematic_talk(npcId=11003146, msg='$52000101_QD__52000101__7$', duration=4000, align='right')
        set_onetime_effect(id=3000947, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000947.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 케이틀린화남05()


class 케이틀린화남05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1200], returnView=False)
        add_cinematic_talk(npcId=11003146, msg='$52000101_QD__52000101__8$', duration=4000, align='right')
        set_onetime_effect(id=3000948, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000948.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 케이틀린화남05_1()


class 케이틀린화남05_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 케이틀린화남06()


class 케이틀린화남06(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=52000100, portalId=1)


