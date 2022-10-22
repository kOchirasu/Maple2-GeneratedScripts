""" trigger/52000100_qd/52000100.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[200], arg2=False) # 아노스
        set_effect(triggerIds=[901], visible=False)
        set_effect(triggerIds=[902], visible=False)
        set_effect(triggerIds=[903], visible=False)
        set_effect(triggerIds=[904], visible=False)
        set_effect(triggerIds=[905], visible=False)
        set_effect(triggerIds=[906], visible=False)
        set_effect(triggerIds=[907], visible=False)
        set_effect(triggerIds=[908], visible=False)
        set_effect(triggerIds=[909], visible=False)
        set_effect(triggerIds=[5305], visible=False) # 경로 안내
        set_effect(triggerIds=[5306], visible=False) # 경로 안내
        set_effect(triggerIds=[5307], visible=False) # 경로 안내
        set_effect(triggerIds=[5308], visible=False) # 경로 안내
        set_effect(triggerIds=[5309], visible=False) # 경로 안내
        set_effect(triggerIds=[5310], visible=False) # 경로 안내
        set_effect(triggerIds=[5305], visible=False) # 경로 안내
        set_effect(triggerIds=[5400], visible=False) # 경로 안내
        set_effect(triggerIds=[5401], visible=False) # 경로 안내
        set_effect(triggerIds=[5402], visible=False) # 경로 안내
        set_effect(triggerIds=[5403], visible=False) # 경로 안내
        set_effect(triggerIds=[5404], visible=False) # 경로 안내
        set_effect(triggerIds=[5405], visible=False) # 경로 안내
        set_effect(triggerIds=[5406], visible=False) # 경로 안내
        set_effect(triggerIds=[5407], visible=False) # 경로 안내

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002290], questStates=[3]):
            return 케이틀린대련01()
        if quest_user_detected(boxIds=[9001], questIds=[20002292], questStates=[2]):
            return 아시모프와대화01()
        if quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[1]):
            return 케이틀린대련04()
        if quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[2]):
            return 대련종료씬시작02()
        if quest_user_detected(boxIds=[9001], questIds=[20002290], questStates=[1]):
            return 몬스터소환교육04()
        if quest_user_detected(boxIds=[9003], questIds=[20002286], questStates=[2]):
            return 강의실입장01()
        if quest_user_detected(boxIds=[9001], questIds=[20002287], questStates=[1]):
            return 참교육01()
        if quest_user_detected(boxIds=[9001], questIds=[20002288], questStates=[1]):
            return 참교육02()
        if quest_user_detected(boxIds=[9001], questIds=[20002289], questStates=[1]):
            return 몬스터소환교육01()


class 강의실입장01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5305], visible=True) # 경로 안내
        set_effect(triggerIds=[5306], visible=True) # 경로 안내
        set_effect(triggerIds=[5307], visible=True) # 경로 안내
        set_effect(triggerIds=[5308], visible=True) # 경로 안내
        set_effect(triggerIds=[5309], visible=True) # 경로 안내
        set_effect(triggerIds=[5310], visible=True) # 경로 안내

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002286], questStates=[2]):
            return 아노스등장01()


class 아노스등장01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        move_user(mapId=52000100, portalId=3)
        set_effect(triggerIds=[5305], visible=False) # 경로 안내
        set_effect(triggerIds=[5306], visible=False) # 경로 안내
        set_effect(triggerIds=[5307], visible=False) # 경로 안내
        set_effect(triggerIds=[5308], visible=False) # 경로 안내
        set_effect(triggerIds=[5309], visible=False) # 경로 안내
        set_effect(triggerIds=[5310], visible=False) # 경로 안내

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아노스등장02()


class 아노스등장02(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_pc_emotion_loop(sequenceName='Emotion_Disappoint_Idle_A', duration=2000)
        select_camera_path(pathIds=[4000,4001], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003148, illustId='Anos_normal', msg='$52000100_QD__52000100__0$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 아노스등장03()


class 아노스등장03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)
        show_caption(type='NameCaption', title='$52000100_QD__52000100__1$', desc='$52000100_QD__52000100__2$', align='center', offsetRateX=-0.05, offsetRateY=0.15, duration=10000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 아노스등장03_1()


class 아노스등장03_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아노스등장04()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아노스등장04()


class 아노스등장04(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0.5)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=25201001, textId=25201001, duration=8000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002287], questStates=[1]):
            return 참교육01()


class 참교육01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25201002, textId=25201002, duration=8000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002288], questStates=[1]):
            return 참교육02()


class 참교육02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5400], visible=True) # 경로 안내
        set_effect(triggerIds=[5401], visible=True) # 경로 안내
        set_effect(triggerIds=[5402], visible=True) # 경로 안내
        set_effect(triggerIds=[5403], visible=True) # 경로 안내
        set_effect(triggerIds=[5404], visible=True) # 경로 안내
        set_effect(triggerIds=[5405], visible=True) # 경로 안내
        set_effect(triggerIds=[5406], visible=True) # 경로 안내
        set_effect(triggerIds=[5407], visible=True) # 경로 안내
        show_guide_summary(entityId=25201003, textId=25201003, duration=8000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002288], questStates=[2]):
            return 참교육완료()


class 참교육완료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5400], visible=False) # 경로 안내
        set_effect(triggerIds=[5401], visible=False) # 경로 안내
        set_effect(triggerIds=[5402], visible=False) # 경로 안내
        set_effect(triggerIds=[5403], visible=False) # 경로 안내
        set_effect(triggerIds=[5404], visible=False) # 경로 안내
        set_effect(triggerIds=[5405], visible=False) # 경로 안내
        set_effect(triggerIds=[5406], visible=False) # 경로 안내
        set_effect(triggerIds=[5407], visible=False) # 경로 안내
        show_guide_summary(entityId=25201003, textId=25201003, duration=8000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002289], questStates=[1]):
            return 몬스터소환교육01()


#  ########################씬2 몬스터 소환 교육01~02########################
class 몬스터소환교육01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5400], visible=False) # 경로 안내
        set_effect(triggerIds=[5401], visible=False) # 경로 안내
        set_effect(triggerIds=[5402], visible=False) # 경로 안내
        set_effect(triggerIds=[5403], visible=False) # 경로 안내
        set_effect(triggerIds=[5404], visible=False) # 경로 안내
        set_effect(triggerIds=[5405], visible=False) # 경로 안내
        set_effect(triggerIds=[5406], visible=False) # 경로 안내
        set_effect(triggerIds=[5407], visible=False) # 경로 안내
        create_monster(spawnIds=[300,301,302,303,304,305], arg2=False)
        move_npc(spawnId=203, patrolName='MS2PatrolData_caitSneak') # 케이틀린 이동
        show_guide_summary(entityId=25201004, textId=25201004, duration=5000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[300,301,302,303,304,305]):
            return 몬스터소환교육02()


class 몬스터소환교육02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002290], questStates=[1]):
            return 몬스터소환교육04()


class 몬스터소환교육04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[400,401,402,403,404,405], arg2=False)
        show_guide_summary(entityId=25201005, textId=25201005, duration=5000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002290], questStates=[3]):
            return 케이틀린대련01()


#  ########################씬3 케이틀린 대련########################
class 케이틀린대련01(state.State):
    def on_enter(self):
        set_sound(triggerId=9006, arg2=True) # 케이틀린 등장 브금
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[203], arg2=False) # 케이틀린
        move_npc(spawnId=203, patrolName='MS2PatrolData_caitComeOut') # 케이틀린 이동
        select_camera_path(pathIds=[4003,4004], returnView=False)
        move_npc(spawnId=200, patrolName='MS2PatrolData_turnAnos')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 케이틀린대련02()


class 케이틀린대련02(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_2, arg2='nextState')
        face_emotion(spawnId=200, emotionName='UpSet')
        add_cinematic_talk(npcId=11003146, illustId='Caitlyn_normal', msg='$52000100_QD__52000100__3$', duration=4000, align='right')
        set_onetime_effect(id=3000950, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000950.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 케이틀린대련03()


class 케이틀린대련03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003146, illustId='Caitlyn_normal', msg='$52000100_QD__52000100__4$', duration=4000, align='right')
        set_onetime_effect(id=3000951, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000951.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 케이틀린대련03_b()


class 케이틀린대련03_b(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003146, illustId='Caitlyn_normal', msg='$52000100_QD__52000100__5$', duration=4000, align='right')
        set_onetime_effect(id=3000952, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000952.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 케이틀린대련03_b_1()


class 케이틀린대련03_b_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 케이틀린대련03_c()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 케이틀린대련03_c()


class 케이틀린대련03_c(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0.5)
        show_guide_summary(entityId=25201006, textId=25201006, duration=5000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[3]):
            return 대련종료씬시작01()
        if quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[2]):
            return 대련종료씬시작01()
        if quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[1]):
            return 케이틀린대련04()


class 케이틀린대련04(state.State):
    def on_enter(self):
        add_buff(boxIds=[9003], skillId=70000109, level=1, arg4=False, arg5=False) # 초생회
        set_sound(triggerId=9006, arg2=True) # 케이틀린 대련 브금
        destroy_monster(spawnIds=[203])
        create_monster(spawnIds=[500], arg2=False) # 케이틀린
        show_guide_summary(entityId=25201007, textId=25201007, duration=5000)
        add_buff(boxIds=[9001], skillId=99910231, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 케이틀린대련05()


class 케이틀린대련05(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25201008, textId=25201008, duration=5000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[500]):
            return 대련종료씬시작01()


class 대련종료씬시작01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        destroy_monster(spawnIds=[203])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 대련종료씬시작02()


#  ########################대련 종료씬########################
class 대련종료씬시작02(state.State):
    def on_enter(self):
        remove_buff(boxId=9001, skillId=99910231)
        set_cinematic_ui(type=1)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        create_monster(spawnIds=[501], arg2=False)
        move_user(mapId=52000100, portalId=4)
        move_npc(spawnId=501, patrolName='MS2PatrolData_caitRun')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 대련종료씬시작03()


class 대련종료씬시작03(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_3, arg2='nextState')
        move_user_path(patrolName='MS2PatrolData_PCRun')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4005,4006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대련종료씬시작04()


class 대련종료씬시작04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=501, sequenceName='Bore_A')
        set_effect(triggerIds=[902], visible=True)
        set_time_scale(enable=True, startScale=0.6, endScale=0.1, duration=3.5, interpolator=2) # 2초간 느려지기 시작
        select_camera_path(pathIds=[4007,4008], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 대련종료씬시작05()


class 대련종료씬시작05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009,4010,4027], returnView=False)
        set_time_scale(enable=False, startScale=1, endScale=0.1, duration=2.5, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 대련종료씬시작06()


class 대련종료씬시작06(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Wizard_Enterance_A'])
        set_pc_emotion_loop(sequenceName='Wizard_Enterance_A', duration=5000)
        set_effect(triggerIds=[901], visible=True)
        set_time_scale(enable=True, startScale=1, endScale=0.1, duration=5.5, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 대련종료씬시작07()


class 대련종료씬시작07(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=0.1, endScale=0.1, duration=6.5, interpolator=2) # 2초간 느려지기 시작
        set_npc_emotion_loop(spawnId=501, sequenceName='Attack_Idle_A', duration=17500)
        set_pc_emotion_loop(sequenceName='Wizard_Enterance_A', duration=5000)
        select_camera_path(pathIds=[4011,4012], returnView=False)
        set_effect(triggerIds=[908], visible=True)
        set_effect(triggerIds=[909], visible=True)
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 대련종료씬시작08()


class 대련종료씬시작08(state.State):
    def on_enter(self):
        set_effect(triggerIds=[901], visible=False)
        set_effect(triggerIds=[902], visible=False)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        move_user(mapId=52000100, portalId=5)
        select_camera_path(pathIds=[4013,4014], returnView=False)
        move_npc(spawnId=200, patrolName='MS2PatrolData_anosCare')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 대련종료씬시작09()


class 대련종료씬시작09(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=12000)
        set_skill(triggerIds=[7005], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 대련종료씬시작09_b()


class 대련종료씬시작09_b(state.State):
    def on_enter(self):
        move_npc(spawnId=501, patrolName='MS2PatrolData_caitRun2')
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4015], returnView=False)
        add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__6$', duration=4000, align='right')
        set_onetime_effect(id=3000964, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000964.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대련종료씬시작10()


class 대련종료씬시작10(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4016], returnView=False)
        add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__7$', duration=4000, align='right')
        set_onetime_effect(id=3000965, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000965.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대련종료씬시작11()


class 대련종료씬시작11(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4017], returnView=False)
        add_cinematic_talk(npcId=11003148, msg='$52000100_QD__52000100__8$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대련종료씬시작12()


class 대련종료씬시작12(state.State):
    def on_enter(self):
        face_emotion(spawnId=200, emotionName='Surprised')
        select_camera_path(pathIds=[4018], returnView=False)
        add_cinematic_talk(npcId=11003148, msg='$52000100_QD__52000100__9$', duration=4000, align='right')
        set_effect(triggerIds=[902], visible=True)
        set_effect(triggerIds=[903], visible=True)
        set_effect(triggerIds=[904], visible=True)
        set_effect(triggerIds=[905], visible=True)
        set_effect(triggerIds=[906], visible=True)
        set_effect(triggerIds=[907], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 대련종료씬시작14()


class 대련종료씬시작14(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4019], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 대련종료씬시작15()


class 대련종료씬시작15(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4020,4021], returnView=False)
        add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__10$', duration=4000, align='right')
        set_onetime_effect(id=3000966, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000966.xml')
        move_npc(spawnId=501, patrolName='MS2PatrolData_caitlookBack')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대련종료씬시작17()


class 대련종료씬시작17(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4022,4023], returnView=False)
        add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__11$', duration=4000, align='right')
        set_onetime_effect(id=3000967, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000967.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 대련종료씬시작17_b()


class 대련종료씬시작17_b(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__12$', duration=4000, align='right')
        set_onetime_effect(id=3000968, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000968.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 대련종료씬시작18()


class 대련종료씬시작18(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='$52000100_QD__52000100__13$', duration=6000, delayTick=1000)
        add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__14$', duration=4000, align='right')
        set_onetime_effect(id=3000969, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000969.xml')
        select_camera_path(pathIds=[4024,4025], returnView=False)
        move_npc(spawnId=501, patrolName='MS2PatrolData_caitOut')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대련종료씬시작18_1()


class 대련종료씬시작18_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대련종료()


class Skip_3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        move_npc(spawnId=200, patrolName='MS2PatrolData_anosCare')
        set_effect(triggerIds=[901], visible=False)
        set_effect(triggerIds=[902], visible=False)
        set_effect(triggerIds=[903], visible=False)
        set_effect(triggerIds=[904], visible=False)
        set_effect(triggerIds=[905], visible=False)
        set_effect(triggerIds=[906], visible=False)
        set_effect(triggerIds=[907], visible=False)
        set_effect(triggerIds=[908], visible=False)
        set_effect(triggerIds=[909], visible=False)
        set_effect(triggerIds=[902], visible=True)
        set_effect(triggerIds=[903], visible=True)
        set_effect(triggerIds=[904], visible=True)
        set_effect(triggerIds=[905], visible=True)
        set_effect(triggerIds=[906], visible=True)
        set_effect(triggerIds=[907], visible=True)
        destroy_monster(spawnIds=[501])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대련종료()


class 대련종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[501])
        remove_buff(boxId=9003, skillId=70000109)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[3]):
            return 아시모프와대화01()


#  ########################씬4 아시모프와 대화########################
class 아시모프와대화01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_Pc_stepAside')
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[202], arg2=False)
        move_npc(spawnId=202, patrolName='MS2PatrolData_asmovMove')
        add_balloon_talk(spawnId=202, msg='$52000100_QD__52000100__15$', duration=5000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 아시모프와대화03()


class 아시모프와대화03(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_4, arg2='nextState')
        select_camera_path(pathIds=[4028], returnView=False)
        show_caption(type='NameCaption', title='$52000100_QD__52000100__16$', desc='$52000100_QD__52000100__17$', align='center', offsetRateX=-0.05, offsetRateY=0.15, duration=10000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 아시모프와대화03_1()


class 아시모프와대화03_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아시모프와대화04()


class Skip_4(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        reset_camera(interpolationTime=0.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아시모프와대화04()


class 아시모프와대화04(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2) # 아시모프를 따라 교장실로 향하세요 가이드 추가

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002292], questStates=[2]):
            return 아시모프와대화05()


class 아시모프와대화05(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=202, msg='$52000100_QD__52000100__18$', duration=6000, delayTick=1000)
        move_npc(spawnId=200, patrolName='MS2PatrolData_anos_goRoom')
        move_npc(spawnId=202, patrolName='MS2PatrolData_asimov_goRoom')
        show_guide_summary(entityId=25201009, textId=25201009, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아시모프와대화06()


class 아시모프와대화06(state.State):
    def on_enter(self):
        move_user(mapId=52000102, portalId=1)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9003, spawnIds=[202]):
            return 아시모프와대화04()


