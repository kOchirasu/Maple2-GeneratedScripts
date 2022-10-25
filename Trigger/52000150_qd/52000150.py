""" trigger/52000150_qd/52000150.xml """
import common


class Wait01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[2605], visible=False)
        self.set_effect(triggerIds=[2607], visible=True)
        self.create_monster(spawnIds=[202], animationEffect=False) # 케이틀린
        self.create_monster(spawnIds=[200], animationEffect=False) # 아노스
        self.create_monster(spawnIds=[201], animationEffect=False) # 호르헤

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[50001642], questStates=[1]):
            return 퀘스트완료상태에서접속(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[3]):
            return 퀘스트완료상태에서접속(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[2]):
            return 퀘스트완료상태에서접속(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[1]):
            return Skip_1(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[50001640], questStates=[3]):
            return Wait02(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[50001640], questStates=[2]):
            return Wait02(self.ctx)


class Wait02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 차원의숲전경씬01(self.ctx)


class 차원의숲전경씬01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000150, portalId=11)
        self.select_camera_path(pathIds=[1000,1001,1004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 차원의숲전경씬02_b(self.ctx)


class 차원의숲전경씬02_b(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 차원의숲전경씬02(self.ctx)


class 차원의숲전경씬02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.select_camera_path(pathIds=[1002,1003], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52000150_QD__52000150__8$', desc='$52000150_QD__52000150__9$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5500, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 차원의숲전경씬03(self.ctx)


class 차원의숲전경씬03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 차원의숲전경씬03_1(self.ctx)


class 차원의숲전경씬03_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차원의숲전경씬종료(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52000150, portalId=11)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차원의숲전경씬종료(self.ctx)


class 차원의숲전경씬종료(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_caitMove01') # 케이틀린 이동
        self.add_balloon_talk(spawnId=202, msg='$52000150_QD__52000150__0$', duration=6000, delayTick=1000) # 케이틀린 대사
        self.show_guide_summary(entityId=25201501, textId=25201501, duration=10000) # 가이드 메시지 : 호르헤와 아노스에게 가기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[3]):
            return 아노스흑화01(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[2]):
            return 퀘스트완료상태에서접속(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[1]):
            return 결계흑화연출01(self.ctx)


# ########################씬3 요동치기 시작한 아노스의 결계########################
class 결계흑화연출01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000150, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 결계흑화연출02(self.ctx)


class 결계흑화연출02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 결계흑화연출03(self.ctx)


class 결계흑화연출03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[2608], visible=True)
        self.select_camera_path(pathIds=[3001,3000], returnView=False)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Traped_A,Traped_Idle')
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003439, msg='$52000150_QD__52000150__1$', duration=4000, align='right') # 호르헤 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return 결계흑화연출03_b(self.ctx)


class 결계흑화연출03_b(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=202, emotionName='Bore_A')
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Traped_Idle', duration=999999)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4200):
            return 결계흑화연출04(self.ctx)


class 결계흑화연출04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_A')
        self.select_camera_path(pathIds=[3002,3003], returnView=False)
        self.add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__2$', duration=5000, align='right') # 케이틀린 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 결계흑화연출05(self.ctx)


class 결계흑화연출05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Attack_Idle_A', duration=999999)
        self.set_effect(triggerIds=[2606], visible=True)
        self.select_camera_path(pathIds=[3004,3005], returnView=False)
        self.add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__3$', duration=5000, align='right') # 케이틀린 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 결계흑화연출06(self.ctx)


class 결계흑화연출06(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[2606], visible=True)
        self.select_camera_path(pathIds=[3006,3007], returnView=False)
        self.set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        self.create_monster(spawnIds=[400,401,402,403,404], animationEffect=False, animationDelay=21000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 결계흑화연출07(self.ctx)


class 결계흑화연출07(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[2606], visible=True)
        self.set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        self.select_camera_path(pathIds=[3008,3009,3010], returnView=False)
        self.add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__4$', duration=4000, align='right') # 케이틀린 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 결계흑화연출08(self.ctx)


class 결계흑화연출08(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[2606], visible=True)
        self.set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        self.add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__5$', duration=4000, align='right') # 케이틀린 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 결계흑화연출09(self.ctx)


class 결계흑화연출09(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[2606], visible=True)
        self.set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        self.select_camera_path(pathIds=[3011,3012], returnView=False)
        self.add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__6$', duration=4000, align='right') # 케이틀린 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 결계흑화연출10(self.ctx)


class 결계흑화연출10(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[2606], visible=True)
        self.set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        self.select_camera_path(pathIds=[3013], returnView=False)
        self.add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__7$', duration=4000, align='right') # 케이틀린 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 결계흑화연출10_1(self.ctx)


class 결계흑화연출10_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 결계흑화연출11(self.ctx)


class Skip_2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_effect(triggerIds=[2605], visible=False)
        self.set_effect(triggerIds=[2606], visible=False)
        self.set_effect(triggerIds=[2607], visible=False)
        self.set_effect(triggerIds=[2608], visible=False)
        self.set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=False, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=False, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=False, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        self.set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=False, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        self.move_user(mapId=52000150, portalId=10)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Traped_Idle', duration=999999)
        self.destroy_monster(spawnIds=[400,401,402,403,404])
        self.create_monster(spawnIds=[400,401,402,403,404], animationEffect=False, animationDelay=100)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 결계흑화연출11(self.ctx)


class 결계흑화연출11(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.set_sound(triggerId=9000, enable=True) # 전투 상황 브금
        self.destroy_monster(spawnIds=[202])
        self.create_monster(spawnIds=[700], animationEffect=False)
        self.set_user_value(triggerId=10001, key='52000150', value=1) # 전투 컨텐츠 시작을 위한 벨류 세팅
        self.show_guide_summary(entityId=25201502, textId=25201502, duration=10000) # 전투 가이드 : 결계 주변의 몬스터 섬멸하기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아노스흑화준비(self.ctx)


class 아노스흑화준비(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=10001, key='52000150', value=0) # 전투 컨텐츠 시작을 위한 벨류 세팅

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='52000150monster', value=1):
            return 아노스흑화대기(self.ctx)


class 아노스흑화대기(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[2605], visible=False)
        self.set_effect(triggerIds=[2606], visible=False)
        self.set_effect(triggerIds=[2607], visible=False)
        self.set_effect(triggerIds=[2608], visible=False)
        self.move_user(mapId=52000150, portalId=10)
        self.destroy_monster(spawnIds=[200], arg2=False) # 아노스
        self.destroy_monster(spawnIds=[201], arg2=False) # 호르헤
        self.destroy_monster(spawnIds=[202])
        self.create_monster(spawnIds=[200], animationEffect=False) # 아노스
        self.create_monster(spawnIds=[201], animationEffect=False) # 호르헤
        self.create_monster(spawnIds=[700], animationEffect=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스흑화전대사01(self.ctx)


class 아노스흑화전대사01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=아노스흑화09, action='exit')
        self.select_camera_path(pathIds=[3005], returnView=False)
        self.add_cinematic_talk(npcId=11003440, msg='$52000150_QD__52000150__11$', duration=4000, align='right') # 아노스 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 아노스흑화전대사02(self.ctx)


class 아노스흑화전대사02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003442, illustId='Caitlyn_serious', msg='$52000150_QD__52000150__12$', duration=3000, align='right') # 케이틀린 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스흑화전대사03(self.ctx)


class 아노스흑화전대사03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6000,6001], returnView=False)
        self.add_cinematic_talk(npcId=11003440, msg='$52000150_QD__52000150__13$', duration=3000, align='right') # 아노스 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스흑화전대사04(self.ctx)


class 아노스흑화전대사04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003442, illustId='Caitlyn_serious', msg='$52000150_QD__52000150__14$', duration=3000, align='right') # 케이틀린 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스흑화전대사05(self.ctx)


class 아노스흑화전대사05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003438, illustId='Horrhe_normal', msg='$52000150_QD__52000150__15$', duration=3000, align='left') # 호르헤 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스흑화전대사06(self.ctx)


class 아노스흑화전대사06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6000], returnView=False)
        self.add_cinematic_talk(npcId=11003440, msg='$52000150_QD__52000150__16$', duration=3000, align='right') # 아노스 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스흑화01(self.ctx)


class 퀘스트완료상태에서접속(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아노스흑화09(self.ctx)


# ########################씬6 아노스 흑화########################
class 아노스흑화01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(triggerIds=[2607], visible=False)
        self.set_cinematic_ui(type=1)
        # <action name="SetSceneSkip" arg1="아노스흑화09" arg2="exit"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스흑화02(self.ctx)


class 아노스흑화02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[6000,6001], returnView=False)
        self.set_npc_emotion_sequence(spawnId=200, sequenceName='Event_02_A,Event_02_Idle')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스흑화03(self.ctx)


class 아노스흑화03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6002,6003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스흑화04(self.ctx)


class 아노스흑화04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6004,6005], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아노스흑화05(self.ctx)


class 아노스흑화05(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[2605], visible=True)
        self.destroy_monster(spawnIds=[200])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 아노스흑화06(self.ctx)


class 아노스흑화06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6006,6007,6008], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아노스흑화07(self.ctx)


class 아노스흑화07(common.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=True, startScale=0.5, endScale=0.3, duration=15, interpolator=1) # 2초간 느려지기 시작

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return 아노스흑화08(self.ctx)


class 아노스흑화08(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 아노스흑화08_1(self.ctx)


class 아노스흑화08_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아노스흑화09(self.ctx)


class 아노스흑화09(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000151, portalId=10)


initial_state = Wait01
