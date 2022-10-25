""" trigger/52000108_qd/52000108.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2001], visible=False)
        self.create_monster(spawnIds=[200], animationEffect=False) # 아이샤등장
        self.set_effect(triggerIds=[5000], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5001], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5002], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5003], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5004], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5005], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5006], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5007], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5008], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5009], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5010], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5011], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5012], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5013], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5014], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5015], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5016], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5017], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5018], visible=False) # 경로 안내
        self.set_effect(triggerIds=[4000], visible=False)
        self.set_effect(triggerIds=[4001], visible=False)
        self.set_effect(triggerIds=[4002], visible=False)
        self.set_effect(triggerIds=[4002], visible=False)
        self.set_effect(triggerIds=[4003], visible=False)
        self.set_effect(triggerIds=[4004], visible=False)
        self.set_effect(triggerIds=[4005], visible=False)
        self.set_effect(triggerIds=[4006], visible=False)
        self.set_effect(triggerIds=[4007], visible=False)
        self.set_effect(triggerIds=[4008], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[20002301], questStates=[3]):
            self.move_user(mapId=52000109, portalId=1)
            return None
        if self.quest_user_detected(boxIds=[10010], questIds=[20002297], questStates=[1]):
            return 불끄기퀘스트01(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[20002298], questStates=[1]):
            return 워터슬라임퀘스트01(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[20002300], questStates=[1]):
            return 저항군로봇퀘스트01(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[20002301], questStates=[1]):
            return 저항군로봇퀘스트01(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[20002300], questStates=[3]):
            return 저항군로봇퀘스트01(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[20002299], questStates=[3]):
            return 저항군로봇퀘스트01(self.ctx)


class 불끄기퀘스트01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[2000], returnView=False)
        self.move_user(mapId=52000108, portalId=10)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 불끄기퀘스트02(self.ctx)


class 불끄기퀘스트02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npcId=11003292, illustId='0', msg='$52000108_QD__52000108__0$', duration=4000, align='right')
        self.set_onetime_effect(id=3000972, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000972.xml')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_ishaTrun')
        self.move_user_path(patrolName='MS2PatrolData_PCTrun')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 불끄기퀘스트03(self.ctx)


class 불끄기퀘스트03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__1$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 불끄기퀘스트04(self.ctx)


class 불끄기퀘스트04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__2$', duration=4000, align='right')
        self.set_pc_emotion_loop(sequenceName='Emotion_Dance_S', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 불끄기퀘스트05(self.ctx)


class 불끄기퀘스트05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__3$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 불끄기퀘스트06(self.ctx)


class 불끄기퀘스트06(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=9000, enable=True)
        self.select_camera_path(pathIds=[2002], returnView=False)
        self.set_onetime_effect(id=40, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npcId=11003292, illustId='0', msg='$52000108_QD__52000108__4$', duration=6000, align='right')
        self.set_onetime_effect(id=3000973, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000973.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 불끄기퀘스트07(self.ctx)


class 불끄기퀘스트07(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=50, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__5$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 불끄기퀘스트08(self.ctx)


class 불끄기퀘스트08(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003292, illustId='$52000108_QD__52000108__45$', msg='$52000108_QD__52000108__6$', duration=4000, align='right')
        self.set_onetime_effect(id=3000974, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000974.xml')
        self.select_camera_path(pathIds=[2003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 불끄기퀘스트09(self.ctx)


class 불끄기퀘스트09(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=60, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.select_camera_path(pathIds=[2004], returnView=False)
        self.set_mesh(triggerIds=[2001], visible=True)
        self.add_cinematic_talk(npcId=11003292, msg='$52000108_QD__52000108__7$', duration=8000, align='right')
        self.set_onetime_effect(id=3000975, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000975.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9500):
            return 불끄기퀘스트10(self.ctx)


class 불끄기퀘스트10(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2003], returnView=False)
        self.add_cinematic_talk(npcId=11003292, illustId='0', msg='$52000108_QD__52000108__8$', duration=5000, align='right')
        self.set_onetime_effect(id=3000976, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000976.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 불끄기퀘스트11(self.ctx)


class 불끄기퀘스트11(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2008], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__9$', duration=2000, align='right')
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Choice_A'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 불끄기퀘스트12(self.ctx)


class 불끄기퀘스트12(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__10$', duration=4000, align='right')
        self.set_pc_emotion_loop(sequenceName='Snare_A', duration=5000)
        self.face_emotion(spawnId=0, emotionName='PC_OutOfMind_01')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 불끄기퀘스트13(self.ctx)


class 불끄기퀘스트13(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트대기01_20002300(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52000108, portalId=10)
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_ishaTrun')
        self.set_mesh(triggerIds=[2001], visible=True)
        self.reset_camera(interpolationTime=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트대기01_20002300(self.ctx)


class 퀘스트대기01_20002300(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201081, textId=25201081, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[20002298], questStates=[1]):
            return 워터슬라임퀘스트01(self.ctx)


class 워터슬라임퀘스트01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[300,301,302,303,304,305], animationEffect=False)
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_caitSneak') # 케이틀린 이동
        self.show_guide_summary(entityId=25201082, textId=25201082, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[20002299], questStates=[3]):
            return 저항군로봇퀘스트01(self.ctx)


# ########################20002300수락, 반마법세력 저항군 등장########################
class 저항군로봇퀘스트01(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=9000, enable=False)
        self.set_sound(triggerId=9001, enable=True)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[2013,2014], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000108, portalId=12)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 저항군로봇퀘스트02(self.ctx)


class 저항군로봇퀘스트02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__11$', duration=6000, align='right')
        self.set_pc_emotion_loop(sequenceName='Object_React_D', duration=25000)
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_ishaCom')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 저항군로봇퀘스트03(self.ctx)


class 저항군로봇퀘스트03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003292, msg='$52000108_QD__52000108__12$', duration=4000, align='right')
        self.set_onetime_effect(id=3000977, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000977.xml')
        self.select_camera_path(pathIds=[2015], returnView=False)
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_isha_8')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 저항군로봇퀘스트04(self.ctx)


class 저항군로봇퀘스트04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__13$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 저항군로봇퀘스트05(self.ctx)


class 저항군로봇퀘스트05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__14$', duration=4000, align='right')
        self.select_camera_path(pathIds=[2016], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 저항군로봇퀘스트06(self.ctx)


class 저항군로봇퀘스트06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003292, msg='$52000108_QD__52000108__15$', duration=6000, align='right')
        self.set_onetime_effect(id=3000978, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000978.xml')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_isha_9')
        self.select_camera_path(pathIds=[2017,2018], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 저항군로봇퀘스트07(self.ctx)


class 저항군로봇퀘스트07(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__16$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 저항군로봇퀘스트08(self.ctx)


class 저항군로봇퀘스트08(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2028], returnView=False)
        self.add_cinematic_talk(npcId=11003292, msg='$52000108_QD__52000108__17$', duration=6000, align='right')
        self.set_onetime_effect(id=3000979, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000979.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 저항군로봇퀘스트09(self.ctx)


class 저항군로봇퀘스트09(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=9002, enable=True)
        self.set_time_scale(enable=True, startScale=0.1, endScale=0.1, duration=7, interpolator=2)
        self.set_skill(triggerIds=[500], enable=True)
        self.select_camera_path(pathIds=[2010,2019], returnView=False)
        self.set_effect(triggerIds=[4000], visible=True)
        self.set_effect(triggerIds=[4001], visible=True)
        self.set_effect(triggerIds=[4002], visible=True)
        self.move_user_path(patrolName='MS2PatrolData_PC_TurnLeft')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 저항군로봇퀘스트10(self.ctx)


class 저항군로봇퀘스트10(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0, emotionName='PC_OutOfMind_01')
        self.select_camera_path(pathIds=[2031], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__18$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 저항군로봇퀘스트11(self.ctx)


class 저항군로봇퀘스트11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=False) # 체키등장
        self.create_monster(spawnIds=[202], animationEffect=False) # 지그문트등장
        self.create_monster(spawnIds=[206], animationEffect=False) # 헨리테등장
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_Checky')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_sigmund')
        self.move_npc(spawnId=206, patrolName='MS2PatrolData_henry')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_IshaCheck')
        self.select_camera_path(pathIds=[2011,2012], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 저항군로봇퀘스트12a(self.ctx)


class 저항군로봇퀘스트12a(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2029,2030], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 저항군로봇퀘스트12_b(self.ctx)


class 저항군로봇퀘스트12_b(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2020,2021], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 저항군로봇퀘스트12_c(self.ctx)


class 저항군로봇퀘스트12_c(common.Trigger):
    def on_enter(self):
        self.show_caption(type='NameCaption', title='$52000108_QD__52000108__19$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=3500, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4100):
            return 저항군로봇퀘스트13(self.ctx)


class 저항군로봇퀘스트13(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2022,2023], returnView=False)
        self.show_caption(type='NameCaption', title='$52000108_QD__52000108__20$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=3500, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4100):
            return 저항군로봇퀘스트14(self.ctx)


class 저항군로봇퀘스트14(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_B')
        self.select_camera_path(pathIds=[2024,2025], returnView=False)
        self.show_caption(type='NameCaption', title='$52000108_QD__52000108__22$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=3500, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4100):
            return 저항군로봇퀘스트15(self.ctx)


class 저항군로봇퀘스트15(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000108, portalId=11)
        self.select_camera_path(pathIds=[2026,2027], returnView=False)
        self.show_caption(type='NameCaption', title='$52000108_QD__52000108__24$', desc='$52000108_QD__52000108__25$', align='topCenter', duration=4000, scale=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4100):
            return 저항군로봇퀘스트15_1(self.ctx)


class 저항군로봇퀘스트15_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 저항군로봇퀘스트16(self.ctx)


class Skip_2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52000108, portalId=11)
        self.create_monster(spawnIds=[201], animationEffect=False) # 체키등장
        self.create_monster(spawnIds=[202], animationEffect=False) # 지그문트등장
        self.create_monster(spawnIds=[206], animationEffect=False) # 헨리테등장
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_Checky')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_sigmund')
        self.move_npc(spawnId=206, patrolName='MS2PatrolData_henry')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_IshaCheck')
        self.set_skill(triggerIds=[500], enable=True)
        self.set_effect(triggerIds=[4000], visible=True)
        self.set_effect(triggerIds=[4001], visible=True)
        self.set_effect(triggerIds=[4002], visible=True)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 저항군로봇퀘스트16(self.ctx)


class 저항군로봇퀘스트16(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0)
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201083, textId=25201083, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[20002301], questStates=[3]):
            self.move_user(mapId=52000109, portalId=1)
            return None
        if self.quest_user_detected(boxIds=[10010], questIds=[20002301], questStates=[2]):
            return 프로토콜해피01(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[20002301], questStates=[1]):
            return 체키등판퀘스트01(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[20002300], questStates=[1]):
            return 저항군로봇퀘스트17(self.ctx)


class 저항군로봇퀘스트17(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_sigmund_back')
        self.create_monster(spawnIds=[306,307,308,309,310], animationEffect=False)
        self.show_guide_summary(entityId=25201084, textId=25201084, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[20002301], questStates=[1]):
            return 체키등판퀘스트01(self.ctx)


# ########################20002301수락, 체키 등판########################
class 체키등판퀘스트01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[2032,2033], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000108, portalId=11)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_sigmund_back')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 체키등판퀘스트02(self.ctx)


class 체키등판퀘스트02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_3, action='nextState')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npcId=11003191, msg='$52000108_QD__52000108__26$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 체키등판퀘스트03(self.ctx)


class 체키등판퀘스트03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2034,2035], returnView=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_CheckyBoss')
        self.add_cinematic_talk(npcId=11003191, msg='$52000108_QD__52000108__27$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 체키등판퀘스트04(self.ctx)


class 체키등판퀘스트04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2036], returnView=False)
        self.add_cinematic_talk(npcId=11003184, msg='$52000108_QD__52000108__28$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5459):
            return 체키등판퀘스트05(self.ctx)


class 체키등판퀘스트05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2037,2038], returnView=False)
        self.add_cinematic_talk(npcId=11003191, msg='$52000108_QD__52000108__29$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 체키등판퀘스트06(self.ctx)


class 체키등판퀘스트06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2039,2040], returnView=False)
        self.add_cinematic_talk(npcId=11003184, msg='$52000108_QD__52000108__30$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4388):
            return 체키등판퀘스트06_1(self.ctx)


class 체키등판퀘스트06_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 체키등판퀘스트07(self.ctx)


class Skip_3(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_CheckyBoss')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 체키등판퀘스트07(self.ctx)


class 체키등판퀘스트07(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[311], animationEffect=False)
        self.add_balloon_talk(spawnId=0, msg='$52000108_QD__52000108__31$', duration=5000, delayTick=1000)
        self.add_balloon_talk(spawnId=205, msg='$52000108_QD__52000108__32$', duration=6000, delayTick=4000)
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_IshaOut')
        self.show_guide_summary(entityId=25201085, textId=25201085, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[20002301], questStates=[2]):
            return 프로토콜해피01(self.ctx)


# ########################코어폭발씬########################
class 프로토콜해피01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[2041,2042], returnView=False)
        self.move_user(mapId=52000108, portalId=11)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[200,201,202,311])
        self.create_monster(spawnIds=[208,209,210], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 프로토콜해피02(self.ctx)


class 프로토콜해피02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_4, action='nextState')
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npcId=11003191, msg='$52000108_QD__52000108__33$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 프로토콜해피03(self.ctx)


class 프로토콜해피03(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_PC_front')
        self.select_camera_path(pathIds=[2043], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__34$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 프로토콜해피04(self.ctx)


class 프로토콜해피04(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0, emotionName='ChaosMod_Start')
        self.select_camera_path(pathIds=[2044], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__35$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 프로토콜해피05(self.ctx)


class 프로토콜해피05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=208, sequenceName='Attack_Idle_A', duration=20000)
        self.select_camera_path(pathIds=[2045,2046], returnView=False)
        self.add_cinematic_talk(npcId=11003292, msg='$52000108_QD__52000108__36$', duration=4000, align='right')
        self.set_onetime_effect(id=3000980, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000980.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 프로토콜해피06(self.ctx)


class 프로토콜해피06(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0)
        self.select_camera_path(pathIds=[2047], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__37$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 프로토콜해피07(self.ctx)


class 프로토콜해피07(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=209, emotionName='Surprised')
        self.select_camera_path(pathIds=[2048], returnView=False)
        self.add_cinematic_talk(npcId=11003183, msg='$52000108_QD__52000108__38$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 프로토콜해피08(self.ctx)


class 프로토콜해피08(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2049,2050], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__39$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 프로토콜해피09(self.ctx)


class 프로토콜해피09(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2051,2053], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000108_QD__52000108__40$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 프로토콜해피10(self.ctx)


class 프로토콜해피10(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=209, sequenceName='Bore_A')
        self.select_camera_path(pathIds=[2052], returnView=False)
        self.add_cinematic_talk(npcId=11003183, msg='$52000108_QD__52000108__41$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 프로토콜해피10_1(self.ctx)


class 프로토콜해피10_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 프로토콜해피11(self.ctx)


class Skip_4(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolationTime=1)
        self.move_user(mapId=52000108, portalId=11)
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 프로토콜해피11(self.ctx)


class 프로토콜해피11(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[4003], visible=True)
        self.set_effect(triggerIds=[4004], visible=True)
        self.set_effect(triggerIds=[4005], visible=True)
        self.set_effect(triggerIds=[4006], visible=True)
        self.set_effect(triggerIds=[4007], visible=True)
        self.set_effect(triggerIds=[4008], visible=True)
        self.destroy_monster(spawnIds=[209,210,206])
        self.set_effect(triggerIds=[5000], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5001], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5002], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5003], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5004], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5005], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5006], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5007], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5008], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5009], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5010], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5011], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5012], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5013], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5014], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5015], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5016], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5017], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5018], visible=True) # 경로 안내
        self.destroy_monster(spawnIds=[208])
        self.create_monster(spawnIds=[211])
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.add_balloon_talk(spawnId=0, msg='$52000108_QD__52000108__42$', duration=6000, delayTick=1000)
        self.show_guide_summary(entityId=25201086, textId=25201086, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10011]):
            return 프로토콜해피12(self.ctx)


class 프로토콜해피12(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=211, msg='$52000108_QD__52000108__43$', duration=6000, delayTick=1000)
        self.set_onetime_effect(id=3000981, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000981.xml')
        self.show_guide_summary(entityId=25201086, textId=25201086, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[20002301], questStates=[3]):
            return 프로토콜해피13(self.ctx)


class 프로토콜해피13(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=211, patrolName='MS2PatrolData_fallback')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 프로토콜해피14(self.ctx)


class 프로토콜해피14(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[211])
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 프로토콜해피13(self.ctx)


initial_state = Wait
