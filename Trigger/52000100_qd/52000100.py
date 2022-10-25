""" trigger/52000100_qd/52000100.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[200], animationEffect=False) # 아노스
        self.set_effect(triggerIds=[901], visible=False)
        self.set_effect(triggerIds=[902], visible=False)
        self.set_effect(triggerIds=[903], visible=False)
        self.set_effect(triggerIds=[904], visible=False)
        self.set_effect(triggerIds=[905], visible=False)
        self.set_effect(triggerIds=[906], visible=False)
        self.set_effect(triggerIds=[907], visible=False)
        self.set_effect(triggerIds=[908], visible=False)
        self.set_effect(triggerIds=[909], visible=False)
        self.set_effect(triggerIds=[5305], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5306], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5307], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5308], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5309], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5310], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5305], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5400], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5401], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5402], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5403], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5404], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5405], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5406], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5407], visible=False) # 경로 안내

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002290], questStates=[3]):
            return 케이틀린대련01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002292], questStates=[2]):
            return 아시모프와대화01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[1]):
            return 케이틀린대련04(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[2]):
            return 대련종료씬시작02(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002290], questStates=[1]):
            return 몬스터소환교육04(self.ctx)
        if self.quest_user_detected(boxIds=[9003], questIds=[20002286], questStates=[2]):
            return 강의실입장01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002287], questStates=[1]):
            return 참교육01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002288], questStates=[1]):
            return 참교육02(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002289], questStates=[1]):
            return 몬스터소환교육01(self.ctx)


class 강의실입장01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5305], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5306], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5307], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5308], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5309], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5310], visible=True) # 경로 안내

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002286], questStates=[2]):
            return 아노스등장01(self.ctx)


class 아노스등장01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000100, portalId=3)
        self.set_effect(triggerIds=[5305], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5306], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5307], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5308], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5309], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5310], visible=False) # 경로 안내

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아노스등장02(self.ctx)


class 아노스등장02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_pc_emotion_loop(sequenceName='Emotion_Disappoint_Idle_A', duration=2000)
        self.select_camera_path(pathIds=[4000,4001], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003148, illustId='Anos_normal', msg='$52000100_QD__52000100__0$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 아노스등장03(self.ctx)


class 아노스등장03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.show_caption(type='NameCaption', title='$52000100_QD__52000100__1$', desc='$52000100_QD__52000100__2$', align='center', offsetRateX=-0.05, offsetRateY=0.15, duration=10000, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 아노스등장03_1(self.ctx)


class 아노스등장03_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아노스등장04(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아노스등장04(self.ctx)


class 아노스등장04(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201001, textId=25201001, duration=8000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002287], questStates=[1]):
            return 참교육01(self.ctx)


class 참교육01(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25201002, textId=25201002, duration=8000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002288], questStates=[1]):
            return 참교육02(self.ctx)


class 참교육02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5400], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5401], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5402], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5403], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5404], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5405], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5406], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5407], visible=True) # 경로 안내
        self.show_guide_summary(entityId=25201003, textId=25201003, duration=8000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002288], questStates=[2]):
            return 참교육완료(self.ctx)


class 참교육완료(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5400], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5401], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5402], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5403], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5404], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5405], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5406], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5407], visible=False) # 경로 안내
        self.show_guide_summary(entityId=25201003, textId=25201003, duration=8000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002289], questStates=[1]):
            return 몬스터소환교육01(self.ctx)


# ########################씬2 몬스터 소환 교육01~02########################
class 몬스터소환교육01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5400], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5401], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5402], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5403], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5404], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5405], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5406], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5407], visible=False) # 경로 안내
        self.create_monster(spawnIds=[300,301,302,303,304,305], animationEffect=False)
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_caitSneak') # 케이틀린 이동
        self.show_guide_summary(entityId=25201004, textId=25201004, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[300,301,302,303,304,305]):
            return 몬스터소환교육02(self.ctx)


class 몬스터소환교육02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002290], questStates=[1]):
            return 몬스터소환교육04(self.ctx)


class 몬스터소환교육04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[400,401,402,403,404,405], animationEffect=False)
        self.show_guide_summary(entityId=25201005, textId=25201005, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002290], questStates=[3]):
            return 케이틀린대련01(self.ctx)


# ########################씬3 케이틀린 대련########################
class 케이틀린대련01(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=9006, enable=True) # 케이틀린 등장 브금
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[203], animationEffect=False) # 케이틀린
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_caitComeOut') # 케이틀린 이동
        self.select_camera_path(pathIds=[4003,4004], returnView=False)
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_turnAnos')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 케이틀린대련02(self.ctx)


class 케이틀린대련02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.face_emotion(spawnId=200, emotionName='UpSet')
        self.add_cinematic_talk(npcId=11003146, illustId='Caitlyn_normal', msg='$52000100_QD__52000100__3$', duration=4000, align='right')
        self.set_onetime_effect(id=3000950, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000950.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 케이틀린대련03(self.ctx)


class 케이틀린대련03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003146, illustId='Caitlyn_normal', msg='$52000100_QD__52000100__4$', duration=4000, align='right')
        self.set_onetime_effect(id=3000951, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000951.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 케이틀린대련03_b(self.ctx)


class 케이틀린대련03_b(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003146, illustId='Caitlyn_normal', msg='$52000100_QD__52000100__5$', duration=4000, align='right')
        self.set_onetime_effect(id=3000952, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000952.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 케이틀린대련03_b_1(self.ctx)


class 케이틀린대련03_b_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 케이틀린대련03_c(self.ctx)


class Skip_2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 케이틀린대련03_c(self.ctx)


class 케이틀린대련03_c(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0.5)
        self.show_guide_summary(entityId=25201006, textId=25201006, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[3]):
            return 대련종료씬시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[2]):
            return 대련종료씬시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[1]):
            return 케이틀린대련04(self.ctx)


class 케이틀린대련04(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9003], skillId=70000109, level=1, isPlayer=False, isSkillSet=False) # 초생회
        self.set_sound(triggerId=9006, enable=True) # 케이틀린 대련 브금
        self.destroy_monster(spawnIds=[203])
        self.create_monster(spawnIds=[500], animationEffect=False) # 케이틀린
        self.show_guide_summary(entityId=25201007, textId=25201007, duration=5000)
        self.add_buff(boxIds=[9001], skillId=99910231, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 케이틀린대련05(self.ctx)


class 케이틀린대련05(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25201008, textId=25201008, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[500]):
            return 대련종료씬시작01(self.ctx)


class 대련종료씬시작01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.destroy_monster(spawnIds=[203])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 대련종료씬시작02(self.ctx)


# ########################대련 종료씬########################
class 대련종료씬시작02(common.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=9001, skillId=99910231)
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.create_monster(spawnIds=[501], animationEffect=False)
        self.move_user(mapId=52000100, portalId=4)
        self.move_npc(spawnId=501, patrolName='MS2PatrolData_caitRun')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 대련종료씬시작03(self.ctx)


class 대련종료씬시작03(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_3, action='nextState')
        self.move_user_path(patrolName='MS2PatrolData_PCRun')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4005,4006], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대련종료씬시작04(self.ctx)


class 대련종료씬시작04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=501, sequenceName='Bore_A')
        self.set_effect(triggerIds=[902], visible=True)
        self.set_time_scale(enable=True, startScale=0.6, endScale=0.1, duration=3.5, interpolator=2) # 2초간 느려지기 시작
        self.select_camera_path(pathIds=[4007,4008], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return 대련종료씬시작05(self.ctx)


class 대련종료씬시작05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4009,4010,4027], returnView=False)
        self.set_time_scale(enable=False, startScale=1, endScale=0.1, duration=2.5, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 대련종료씬시작06(self.ctx)


class 대련종료씬시작06(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Wizard_Enterance_A'])
        self.set_pc_emotion_loop(sequenceName='Wizard_Enterance_A', duration=5000)
        self.set_effect(triggerIds=[901], visible=True)
        self.set_time_scale(enable=True, startScale=1, endScale=0.1, duration=5.5, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 대련종료씬시작07(self.ctx)


class 대련종료씬시작07(common.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=True, startScale=0.1, endScale=0.1, duration=6.5, interpolator=2) # 2초간 느려지기 시작
        self.set_npc_emotion_loop(spawnId=501, sequenceName='Attack_Idle_A', duration=17500)
        self.set_pc_emotion_loop(sequenceName='Wizard_Enterance_A', duration=5000)
        self.select_camera_path(pathIds=[4011,4012], returnView=False)
        self.set_effect(triggerIds=[908], visible=True)
        self.set_effect(triggerIds=[909], visible=True)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6500):
            return 대련종료씬시작08(self.ctx)


class 대련종료씬시작08(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[901], visible=False)
        self.set_effect(triggerIds=[902], visible=False)
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.move_user(mapId=52000100, portalId=5)
        self.select_camera_path(pathIds=[4013,4014], returnView=False)
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_anosCare')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 대련종료씬시작09(self.ctx)


class 대련종료씬시작09(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=12000)
        self.set_skill(triggerIds=[7005], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 대련종료씬시작09_b(self.ctx)


class 대련종료씬시작09_b(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=501, patrolName='MS2PatrolData_caitRun2')
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4015], returnView=False)
        self.add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__6$', duration=4000, align='right')
        self.set_onetime_effect(id=3000964, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000964.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대련종료씬시작10(self.ctx)


class 대련종료씬시작10(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4016], returnView=False)
        self.add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__7$', duration=4000, align='right')
        self.set_onetime_effect(id=3000965, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000965.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대련종료씬시작11(self.ctx)


class 대련종료씬시작11(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4017], returnView=False)
        self.add_cinematic_talk(npcId=11003148, msg='$52000100_QD__52000100__8$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대련종료씬시작12(self.ctx)


class 대련종료씬시작12(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=200, emotionName='Surprised')
        self.select_camera_path(pathIds=[4018], returnView=False)
        self.add_cinematic_talk(npcId=11003148, msg='$52000100_QD__52000100__9$', duration=4000, align='right')
        self.set_effect(triggerIds=[902], visible=True)
        self.set_effect(triggerIds=[903], visible=True)
        self.set_effect(triggerIds=[904], visible=True)
        self.set_effect(triggerIds=[905], visible=True)
        self.set_effect(triggerIds=[906], visible=True)
        self.set_effect(triggerIds=[907], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대련종료씬시작14(self.ctx)


class 대련종료씬시작14(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4019], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대련종료씬시작15(self.ctx)


class 대련종료씬시작15(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4020,4021], returnView=False)
        self.add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__10$', duration=4000, align='right')
        self.set_onetime_effect(id=3000966, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000966.xml')
        self.move_npc(spawnId=501, patrolName='MS2PatrolData_caitlookBack')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대련종료씬시작17(self.ctx)


class 대련종료씬시작17(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4022,4023], returnView=False)
        self.add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__11$', duration=4000, align='right')
        self.set_onetime_effect(id=3000967, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000967.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대련종료씬시작17_b(self.ctx)


class 대련종료씬시작17_b(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__12$', duration=4000, align='right')
        self.set_onetime_effect(id=3000968, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000968.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return 대련종료씬시작18(self.ctx)


class 대련종료씬시작18(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$52000100_QD__52000100__13$', duration=6000, delayTick=1000)
        self.add_cinematic_talk(npcId=11003147, msg='$52000100_QD__52000100__14$', duration=4000, align='right')
        self.set_onetime_effect(id=3000969, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000969.xml')
        self.select_camera_path(pathIds=[4024,4025], returnView=False)
        self.move_npc(spawnId=501, patrolName='MS2PatrolData_caitOut')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대련종료씬시작18_1(self.ctx)


class 대련종료씬시작18_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대련종료(self.ctx)


class Skip_3(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_anosCare')
        self.set_effect(triggerIds=[901], visible=False)
        self.set_effect(triggerIds=[902], visible=False)
        self.set_effect(triggerIds=[903], visible=False)
        self.set_effect(triggerIds=[904], visible=False)
        self.set_effect(triggerIds=[905], visible=False)
        self.set_effect(triggerIds=[906], visible=False)
        self.set_effect(triggerIds=[907], visible=False)
        self.set_effect(triggerIds=[908], visible=False)
        self.set_effect(triggerIds=[909], visible=False)
        self.set_effect(triggerIds=[902], visible=True)
        self.set_effect(triggerIds=[903], visible=True)
        self.set_effect(triggerIds=[904], visible=True)
        self.set_effect(triggerIds=[905], visible=True)
        self.set_effect(triggerIds=[906], visible=True)
        self.set_effect(triggerIds=[907], visible=True)
        self.destroy_monster(spawnIds=[501])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대련종료(self.ctx)


class 대련종료(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[501])
        self.remove_buff(boxId=9003, skillId=70000109)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002291], questStates=[3]):
            return 아시모프와대화01(self.ctx)


# ########################씬4 아시모프와 대화########################
class 아시모프와대화01(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_Pc_stepAside')
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_asmovMove')
        self.add_balloon_talk(spawnId=202, msg='$52000100_QD__52000100__15$', duration=5000, delayTick=1000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 아시모프와대화03(self.ctx)


class 아시모프와대화03(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_4, action='nextState')
        self.select_camera_path(pathIds=[4028], returnView=False)
        self.show_caption(type='NameCaption', title='$52000100_QD__52000100__16$', desc='$52000100_QD__52000100__17$', align='center', offsetRateX=-0.05, offsetRateY=0.15, duration=10000, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 아시모프와대화03_1(self.ctx)


class 아시모프와대화03_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아시모프와대화04(self.ctx)


class Skip_4(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolationTime=0.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아시모프와대화04(self.ctx)


class 아시모프와대화04(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2) # 아시모프를 따라 교장실로 향하세요 가이드 추가

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002292], questStates=[2]):
            return 아시모프와대화05(self.ctx)


class 아시모프와대화05(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=202, msg='$52000100_QD__52000100__18$', duration=6000, delayTick=1000)
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_anos_goRoom')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_asimov_goRoom')
        self.show_guide_summary(entityId=25201009, textId=25201009, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아시모프와대화06(self.ctx)


class 아시모프와대화06(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000102, portalId=1)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9003, spawnIds=[202]):
            return 아시모프와대화04(self.ctx)


initial_state = Wait
