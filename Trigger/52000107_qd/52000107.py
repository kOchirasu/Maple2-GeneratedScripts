""" trigger/52000107_qd/52000107.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5304], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5305], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5306], visible=False) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5307], visible=False) # 목표 바닥 지점01 NPC
        self.set_effect(triggerIds=[5308], visible=False) # 목표 바닥 지점03 포탈
        self.set_effect(triggerIds=[5309], visible=False) # 화살표01 NPC
        self.set_effect(triggerIds=[5310], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5311], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5312], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5313], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5314], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5315], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5316], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5317], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5318], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5319], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5320], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5321], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5322], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5323], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5324], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5325], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5326], visible=False) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[10010]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000107, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='common\JobIntro_HeavyGunner.usm', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 에델슈타인전경씬01(self.ctx)
        if self.wait_tick(waitTick=42000):
            return 에델슈타인전경씬01(self.ctx)


class 에델슈타인전경씬01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[1000,1001], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8500):
            return 에델슈타인전경씬01_B(self.ctx)


class 에델슈타인전경씬01_B(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 에델슈타인전경씬02(self.ctx)


class 에델슈타인전경씬02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[1002,1003,1004,1005], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 에델슈타인전경씬03(self.ctx)


class 에델슈타인전경씬03(trigger_api.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000107_QD__52000107__0$', desc='$52000107_QD__52000107__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에델슈타인전경씬04(self.ctx)


class 에델슈타인전경씬04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.set_effect(triggerIds=[5304], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5305], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5306], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5307], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5308], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5309], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5310], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5311], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5312], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5313], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5314], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5315], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5316], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5317], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5318], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5319], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5320], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5321], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5322], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5323], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5324], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5325], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5326], visible=True) # 경로 안내
        self.add_balloon_talk(spawnId=0, msg='$52000107_QD__52000107__2$', duration=6000, delayTick=1000)
        self.show_guide_summary(entityId=25201071, textId=25201071, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[10011]):
            return 아이샤등장씬01(self.ctx)


# ########################씬2 아이샤 등장########################
class 아이샤등장씬01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[2000], animationEffect=False) # 아이샤등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아이샤등장씬02(self.ctx)


class 아이샤등장씬02(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawnId=2000, patrolName='MS2PatrolData_Ayesha_go')
        self.select_camera_path(pathIds=[1006,1007], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아이샤등장씬04(self.ctx)


class 아이샤등장씬04(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003291, illustId='Ayesha_normal', msg='$52000107_QD__52000107__3$', duration=4000, align='right')
        self.set_onetime_effect(id=3000970, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000970.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 아이샤등장씬05(self.ctx)


class 아이샤등장씬05(trigger_api.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=200, emotionName='hello_Cait')
        self.show_caption(type='NameCaption', title='$52000107_QD__52000107__4$', desc='$52000107_QD__52000107__5$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=10000, scale=2)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 아이샤등장씬06(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아이샤등장씬06(self.ctx)


class 아이샤등장씬06(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.set_effect(triggerIds=[5304], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5305], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5306], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5307], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5308], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5309], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5310], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5311], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5312], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5313], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5314], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5315], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5316], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5317], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5318], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5319], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5320], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5321], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5322], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5323], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5324], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5325], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5326], visible=False) # 경로 안내
        self.face_emotion(spawnId=200)
        self.show_guide_summary(entityId=25201071, textId=25201071, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002296], questStates=[2]):
            return 아이샤와떠남01(self.ctx)


# ########################씬3 아이샤와pc, 퓨전코어 연구실로########################
class 아이샤와떠남01(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=2000, msg='$52000107_QD__52000107__6$', duration=6000, delayTick=1000)
        self.set_onetime_effect(id=3000971, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000971.xml')
        self.move_npc(spawnId=2000, patrolName='MS2PatrolData_Ayesga_out')
        self.show_guide_summary(entityId=25201072, textId=25201072, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=10012, spawnIds=[2000]):
            return 아이샤와떠남02(self.ctx)


class 아이샤와떠남02(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.destroy_monster(spawnIds=[2000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9003, spawnIds=[202]):
            return None # Missing State: 아이샤와떠남03


initial_state = Wait
