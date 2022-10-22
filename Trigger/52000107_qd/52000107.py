""" trigger/52000107_qd/52000107.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
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
        set_effect(triggerIds=[5323], visible=False) # 경로 안내
        set_effect(triggerIds=[5324], visible=False) # 경로 안내
        set_effect(triggerIds=[5325], visible=False) # 경로 안내
        set_effect(triggerIds=[5326], visible=False) # 경로 안내

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10010]):
            return 영상준비_01()


class 영상준비_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        move_user(mapId=52000107, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='common\JobIntro_HeavyGunner.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 에델슈타인전경씬01()
        if wait_tick(waitTick=42000):
            return 에델슈타인전경씬01()


class 에델슈타인전경씬01(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[1000,1001], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8500):
            return 에델슈타인전경씬01_B()


class 에델슈타인전경씬01_B(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에델슈타인전경씬02()


class 에델슈타인전경씬02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[1002,1003,1004,1005], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에델슈타인전경씬03()


class 에델슈타인전경씬03(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000107_QD__52000107__0$', desc='$52000107_QD__52000107__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에델슈타인전경씬04()


class 에델슈타인전경씬04(state.State):
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
        set_effect(triggerIds=[5323], visible=True) # 경로 안내
        set_effect(triggerIds=[5324], visible=True) # 경로 안내
        set_effect(triggerIds=[5325], visible=True) # 경로 안내
        set_effect(triggerIds=[5326], visible=True) # 경로 안내
        add_balloon_talk(spawnId=0, msg='$52000107_QD__52000107__2$', duration=6000, delayTick=1000)
        show_guide_summary(entityId=25201071, textId=25201071, duration=10000)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10011]):
            return 아이샤등장씬01()


#  ########################씬2 아이샤 등장########################
class 아이샤등장씬01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[2000], arg2=False) # 아이샤등장

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아이샤등장씬02()


class 아이샤등장씬02(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_2, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_npc(spawnId=2000, patrolName='MS2PatrolData_Ayesha_go')
        select_camera_path(pathIds=[1006,1007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아이샤등장씬04()


class 아이샤등장씬04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003291, illustId='Ayesha_normal', msg='$52000107_QD__52000107__3$', duration=4000, align='right')
        set_onetime_effect(id=3000970, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000970.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 아이샤등장씬05()


class 아이샤등장씬05(state.State):
    def on_enter(self):
        face_emotion(spawnId=200, emotionName='hello_Cait')
        show_caption(type='NameCaption', title='$52000107_QD__52000107__4$', desc='$52000107_QD__52000107__5$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=10000, scale=2)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 아이샤등장씬06()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아이샤등장씬06()


class 아이샤등장씬06(state.State):
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
        set_effect(triggerIds=[5323], visible=False) # 경로 안내
        set_effect(triggerIds=[5324], visible=False) # 경로 안내
        set_effect(triggerIds=[5325], visible=False) # 경로 안내
        set_effect(triggerIds=[5326], visible=False) # 경로 안내
        face_emotion(spawnId=200)
        show_guide_summary(entityId=25201071, textId=25201071, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002296], questStates=[2]):
            return 아이샤와떠남01()


#  ########################씬3 아이샤와pc, 퓨전코어 연구실로########################
class 아이샤와떠남01(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=2000, msg='$52000107_QD__52000107__6$', duration=6000, delayTick=1000)
        set_onetime_effect(id=3000971, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000971.xml')
        move_npc(spawnId=2000, patrolName='MS2PatrolData_Ayesga_out')
        show_guide_summary(entityId=25201072, textId=25201072, duration=5000)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=10012, spawnIds=[2000]):
            return 아이샤와떠남02()


class 아이샤와떠남02(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        destroy_monster(spawnIds=[2000])

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9003, spawnIds=[202]):
            return None # Missing State: 아이샤와떠남03


