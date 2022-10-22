""" trigger/52000150_qd/52000150.xml """
from common import *
import state


class Wait01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2605], visible=False)
        set_effect(triggerIds=[2607], visible=True)
        create_monster(spawnIds=[202], arg2=False) # 케이틀린
        create_monster(spawnIds=[200], arg2=False) # 아노스
        create_monster(spawnIds=[201], arg2=False) # 호르헤

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10010], questIds=[50001642], questStates=[1]):
            return 퀘스트완료상태에서접속()
        if quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[3]):
            return 퀘스트완료상태에서접속()
        if quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[2]):
            return 퀘스트완료상태에서접속()
        if quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[1]):
            return Skip_1()
        if quest_user_detected(boxIds=[10010], questIds=[50001640], questStates=[3]):
            return Wait02()
        if quest_user_detected(boxIds=[10010], questIds=[50001640], questStates=[2]):
            return Wait02()


class Wait02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 차원의숲전경씬01()


class 차원의숲전경씬01(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        move_user(mapId=52000150, portalId=11)
        select_camera_path(pathIds=[1000,1001,1004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 차원의숲전경씬02_b()


class 차원의숲전경씬02_b(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차원의숲전경씬02()


class 차원의숲전경씬02(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        select_camera_path(pathIds=[1002,1003], returnView=False)
        show_caption(type='VerticalCaption', title='$52000150_QD__52000150__8$', desc='$52000150_QD__52000150__9$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5500, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 차원의숲전경씬03()


class 차원의숲전경씬03(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차원의숲전경씬03_1()


class 차원의숲전경씬03_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차원의숲전경씬종료()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        move_user(mapId=52000150, portalId=11)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차원의숲전경씬종료()


class 차원의숲전경씬종료(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        move_npc(spawnId=202, patrolName='MS2PatrolData_caitMove01') # 케이틀린 이동
        add_balloon_talk(spawnId=202, msg='$52000150_QD__52000150__0$', duration=6000, delayTick=1000) # 케이틀린 대사
        show_guide_summary(entityId=25201501, textId=25201501, duration=10000) # 가이드 메시지 : 호르헤와 아노스에게 가기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[3]):
            return 아노스흑화01()
        if quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[2]):
            return 퀘스트완료상태에서접속()
        if quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[1]):
            return 결계흑화연출01()


#  ########################씬3 요동치기 시작한 아노스의 결계########################
class 결계흑화연출01(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_2, arg2='nextState')
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        move_user(mapId=52000150, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 결계흑화연출02()


class 결계흑화연출02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 결계흑화연출03()


class 결계흑화연출03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2608], visible=True)
        select_camera_path(pathIds=[3001,3000], returnView=False)
        set_npc_emotion_sequence(spawnId=201, sequenceName='Traped_A,Traped_Idle')
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003439, msg='$52000150_QD__52000150__1$', duration=4000, align='right') # 호르헤 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 결계흑화연출03_b()


class 결계흑화연출03_b(state.State):
    def on_enter(self):
        face_emotion(spawnId=202, emotionName='Bore_A')
        set_npc_emotion_loop(spawnId=201, sequenceName='Traped_Idle', duration=999999)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4200):
            return 결계흑화연출04()


class 결계흑화연출04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_A')
        select_camera_path(pathIds=[3002,3003], returnView=False)
        add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__2$', duration=5000, align='right') # 케이틀린 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 결계흑화연출05()


class 결계흑화연출05(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=202, sequenceName='Attack_Idle_A', duration=999999)
        set_effect(triggerIds=[2606], visible=True)
        select_camera_path(pathIds=[3004,3005], returnView=False)
        add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__3$', duration=5000, align='right') # 케이틀린 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 결계흑화연출06()


class 결계흑화연출06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2606], visible=True)
        select_camera_path(pathIds=[3006,3007], returnView=False)
        set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        create_monster(spawnIds=[400,401,402,403,404], arg2=False, arg3=21000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 결계흑화연출07()


class 결계흑화연출07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2606], visible=True)
        set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        select_camera_path(pathIds=[3008,3009,3010], returnView=False)
        add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__4$', duration=4000, align='right') # 케이틀린 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 결계흑화연출08()


class 결계흑화연출08(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2606], visible=True)
        set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__5$', duration=4000, align='right') # 케이틀린 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 결계흑화연출09()


class 결계흑화연출09(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2606], visible=True)
        set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        select_camera_path(pathIds=[3011,3012], returnView=False)
        add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__6$', duration=4000, align='right') # 케이틀린 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 결계흑화연출10()


class 결계흑화연출10(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2606], visible=True)
        set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        select_camera_path(pathIds=[3013], returnView=False)
        add_cinematic_talk(npcId=11003442, msg='$52000150_QD__52000150__7$', duration=4000, align='right') # 케이틀린 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 결계흑화연출10_1()


class 결계흑화연출10_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 결계흑화연출11()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_effect(triggerIds=[2605], visible=False)
        set_effect(triggerIds=[2606], visible=False)
        set_effect(triggerIds=[2607], visible=False)
        set_effect(triggerIds=[2608], visible=False)
        set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=False, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=False, arg3=200, arg4=200) # #####1번 지역 리젠 알림#####
        set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=False, arg3=400, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=False, arg3=600, arg4=200) # #####2번 지역 리젠 알림#####
        move_user(mapId=52000150, portalId=10)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_npc_emotion_loop(spawnId=201, sequenceName='Traped_Idle', duration=999999)
        destroy_monster(spawnIds=[400,401,402,403,404])
        create_monster(spawnIds=[400,401,402,403,404], arg2=False, arg3=100)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 결계흑화연출11()


class 결계흑화연출11(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        set_sound(triggerId=9000, arg2=True) # 전투 상황 브금
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[700], arg2=False)
        set_user_value(triggerId=10001, key='52000150', value=1) # 전투 컨텐츠 시작을 위한 벨류 세팅
        show_guide_summary(entityId=25201502, textId=25201502, duration=10000) # 전투 가이드 : 결계 주변의 몬스터 섬멸하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아노스흑화준비()


class 아노스흑화준비(state.State):
    def on_enter(self):
        set_user_value(triggerId=10001, key='52000150', value=0) # 전투 컨텐츠 시작을 위한 벨류 세팅

    def on_tick(self) -> state.State:
        if user_value(key='52000150monster', value=1):
            return 아노스흑화대기()


class 아노스흑화대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[2605], visible=False)
        set_effect(triggerIds=[2606], visible=False)
        set_effect(triggerIds=[2607], visible=False)
        set_effect(triggerIds=[2608], visible=False)
        move_user(mapId=52000150, portalId=10)
        destroy_monster(spawnIds=[200], arg2=False) # 아노스
        destroy_monster(spawnIds=[201], arg2=False) # 호르헤
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[200], arg2=False) # 아노스
        create_monster(spawnIds=[201], arg2=False) # 호르헤
        create_monster(spawnIds=[700], arg2=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스흑화전대사01()


class 아노스흑화전대사01(state.State):
    def on_enter(self):
        set_scene_skip(state=아노스흑화09, arg2='exit')
        select_camera_path(pathIds=[3005], returnView=False)
        add_cinematic_talk(npcId=11003440, msg='$52000150_QD__52000150__11$', duration=4000, align='right') # 아노스 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 아노스흑화전대사02()


class 아노스흑화전대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003442, illustId='Caitlyn_serious', msg='$52000150_QD__52000150__12$', duration=3000, align='right') # 케이틀린 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스흑화전대사03()


class 아노스흑화전대사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6000,6001], returnView=False)
        add_cinematic_talk(npcId=11003440, msg='$52000150_QD__52000150__13$', duration=3000, align='right') # 아노스 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스흑화전대사04()


class 아노스흑화전대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003442, illustId='Caitlyn_serious', msg='$52000150_QD__52000150__14$', duration=3000, align='right') # 케이틀린 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스흑화전대사05()


class 아노스흑화전대사05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003438, illustId='Horrhe_normal', msg='$52000150_QD__52000150__15$', duration=3000, align='left') # 호르헤 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스흑화전대사06()


class 아노스흑화전대사06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6000], returnView=False)
        add_cinematic_talk(npcId=11003440, msg='$52000150_QD__52000150__16$', duration=3000, align='right') # 아노스 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스흑화01()


class 퀘스트완료상태에서접속(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아노스흑화09()


#  ########################씬6 아노스 흑화########################
class 아노스흑화01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_effect(triggerIds=[2607], visible=False)
        set_cinematic_ui(type=1)
        # <action name="SetSceneSkip" arg1="아노스흑화09" arg2="exit"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스흑화02()


class 아노스흑화02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[6000,6001], returnView=False)
        set_npc_emotion_sequence(spawnId=200, sequenceName='Event_02_A,Event_02_Idle')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스흑화03()


class 아노스흑화03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6002,6003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스흑화04()


class 아노스흑화04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6004,6005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아노스흑화05()


class 아노스흑화05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2605], visible=True)
        destroy_monster(spawnIds=[200])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 아노스흑화06()


class 아노스흑화06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6006,6007,6008], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아노스흑화07()


class 아노스흑화07(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=0.5, endScale=0.3, duration=15, interpolator=1) # 2초간 느려지기 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 아노스흑화08()


class 아노스흑화08(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 아노스흑화08_1()


class 아노스흑화08_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아노스흑화09()


class 아노스흑화09(state.State):
    def on_enter(self):
        move_user(mapId=52000151, portalId=10)


