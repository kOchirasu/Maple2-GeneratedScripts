""" trigger/52010027_qd/main.xml """
import common


# 바람의 골짜기 : 52010027
class idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003073], questStates=[1]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301], animationEffect=True) # 습격지역 꼭대기 집
        self.create_monster(spawnIds=[302], animationEffect=True) # 습격지역 꼭대기 입구
        self.create_monster(spawnIds=[303], animationEffect=True) # 습격지역 꼭대기 주민
        self.create_monster(spawnIds=[304], animationEffect=True) # 진입부 주민 1층
        self.create_monster(spawnIds=[305], animationEffect=True) # 진입부 주민 2층
        self.create_monster(spawnIds=[401], animationEffect=True) # 악당NPC_1
        self.create_monster(spawnIds=[402], animationEffect=True) # 악당NPC_2
        self.create_monster(spawnIds=[403], animationEffect=True) # 악당NPC_3
        self.create_monster(spawnIds=[404], animationEffect=True) # 악당NPC_4
        self.create_monster(spawnIds=[405], animationEffect=True) # 악당NPC_5
        self.create_monster(spawnIds=[406], animationEffect=True) # 악당NPC_6
        self.create_monster(spawnIds=[407], animationEffect=True) # 악당NPC_7
        self.create_monster(spawnIds=[408], animationEffect=True) # 악당NPC_8
        self.create_monster(spawnIds=[409], animationEffect=True) # 악당NPC_9
        self.create_monster(spawnIds=[501], animationEffect=True) # 보스NPC_1
        self.create_monster(spawnIds=[502], animationEffect=True) # 보스NPC_1
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라_전환(self.ctx)


class 카메라_전환(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52010027_QD__MAIN__0$', desc='$52010027_QD__MAIN__1$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        self.set_npc_emotion_loop(spawnId=303, sequenceName='Down_Idle_A', duration=150000)
        self.face_emotion(spawnId=302, emotionName='down_Idle')
        self.face_emotion(spawnId=303, emotionName='down_Idle')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 연출_습격현장(self.ctx)


class 연출_습격현장(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.add_balloon_talk(spawnId=301, msg='$52010027_QD__MAIN__2$', duration=3000, delayTick=0)
        self.add_balloon_talk(spawnId=403, msg='$52010027_QD__MAIN__3$', duration=3000, delayTick=0)
        self.add_balloon_talk(spawnId=303, msg='$52010027_QD__MAIN__4$', duration=2000, delayTick=1000)
        self.set_npc_emotion_sequence(spawnId=402, sequenceName='Attack_02_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4200):
            return 연출_습격현장_02(self.ctx)


class 연출_습격현장_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출_습격현장_02_01(self.ctx)


class 연출_습격현장_02_01(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=401, msg='$52010027_QD__MAIN__5$', duration=2000, delayTick=0)
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Attack_02_A')
        self.add_balloon_talk(spawnId=304, msg='$52010027_QD__MAIN__6$', duration=2000, delayTick=500)
        self.add_balloon_talk(spawnId=305, msg='$52010027_QD__MAIN__7$', duration=3000, delayTick=1500)
        self.set_npc_emotion_loop(spawnId=305, sequenceName='Down_Idle_A', duration=150000)
        self.face_emotion(spawnId=304, emotionName='down_Idle')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return 연출_습격현장확인_PC(self.ctx)


class 연출_습격현장확인_PC(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__8$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__9$', duration=3000)
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=10000)
        self.add_balloon_talk(spawnId=0, msg='$52010027_QD__MAIN__10$', duration=2000, delayTick=6000)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__11$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 연출_습격현장_보스등장(self.ctx)


class 연출_습격현장_보스등장(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4010], returnView=False)
        self.move_npc(spawnId=502, patrolName='MS2PatrolData_3004')
        self.show_caption(type='VerticalCaption', title='$52010027_QD__MAIN__12$', desc='$52010027_QD__MAIN__13$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__14$', duration=3500)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__15$', duration=3500)
        self.add_balloon_talk(spawnId=405, msg='$52010027_QD__MAIN__16$', duration=2000, delayTick=2000)
        self.add_balloon_talk(spawnId=406, msg='$52010027_QD__MAIN__17$', duration=2000, delayTick=1800)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 연출_습격현장_보스이동(self.ctx)


class 연출_습격현장_보스이동(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=501, sequenceName='Attack_01_G')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출_습격현장_보스소환연출(self.ctx)


class 연출_습격현장_보스소환연출(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[502]) # 보스NPC_1
        self.set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출_습격현장_보스소환연출_02(self.ctx)


class 연출_습격현장_보스소환연출_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return 연출_습격현장_보스소환연출_03(self.ctx)


class 연출_습격현장_보스소환연출_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__18$', duration=3000)
        self.set_npc_emotion_sequence(spawnId=501, sequenceName='Attack_01_D')
        self.move_user(mapId=52010027, portalId=6001)
        self.destroy_monster(spawnIds=[401])
        self.destroy_monster(spawnIds=[402])
        self.destroy_monster(spawnIds=[403])
        self.destroy_monster(spawnIds=[404])
        self.destroy_monster(spawnIds=[405])
        self.destroy_monster(spawnIds=[406])
        self.destroy_monster(spawnIds=[407])
        self.destroy_monster(spawnIds=[408])
        self.destroy_monster(spawnIds=[409])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3800):
            return 연출_습격현장_PC연출(self.ctx)


class 연출_습격현장_PC연출(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=3500)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__19$', duration=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출_습격현장_PC연출_1(self.ctx)


class 연출_습격현장_PC연출_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출_습격현장_전투준비(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52010027, portalId=6001)
        self.set_effect(triggerIds=[5002], visible=True)
        self.destroy_monster(spawnIds=[502]) # 보스NPC_1
        self.destroy_monster(spawnIds=[401])
        self.destroy_monster(spawnIds=[402])
        self.destroy_monster(spawnIds=[403])
        self.destroy_monster(spawnIds=[404])
        self.destroy_monster(spawnIds=[405])
        self.destroy_monster(spawnIds=[406])
        self.destroy_monster(spawnIds=[407])
        self.destroy_monster(spawnIds=[408])
        self.destroy_monster(spawnIds=[409])
        self.select_camera_path(pathIds=[4008], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출_습격현장_전투준비(self.ctx)


class 연출_습격현장_전투준비(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[601], animationEffect=True) # 악당Mob_1
        self.create_monster(spawnIds=[602], animationEffect=True) # 악당Mob_2
        self.create_monster(spawnIds=[603], animationEffect=True) # 악당Mob_3
        self.create_monster(spawnIds=[604], animationEffect=True) # 악당Mob_4
        self.create_monster(spawnIds=[605], animationEffect=True) # 악당Mob_5
        self.create_monster(spawnIds=[606], animationEffect=True) # 악당Mob_6
        self.add_balloon_talk(spawnId=602, msg='$52010027_QD__MAIN__20$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=606, msg='$52010027_QD__MAIN__21$', duration=2000, delayTick=500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출_습격현장_전투준비_02(self.ctx)


class 연출_습격현장_전투준비_02(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 차_전투1(self.ctx)


class 차_전투1(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52010027_QD__MAIN__22$', arg3='3000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[601,602,603,604,605,606]):
            return 연출_잠시쉬기(self.ctx)


class 연출_잠시쉬기(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차_전투_보스몬스터대사1(self.ctx)


class 차_전투_보스몬스터대사1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__23$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차_전투_보스소환연출2(self.ctx)


class 차_전투_보스소환연출2(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__24$', duration=3000)
        self.set_npc_emotion_sequence(spawnId=501, sequenceName='Attack_01_C')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차_전투_보스소환연출_1_2(self.ctx)


class 차_전투_보스소환연출_1_2(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차_전투2(self.ctx)


class Skip_2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차_전투2(self.ctx)


class 차_전투2(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui(type=1, arg2='$52010027_QD__MAIN__25$', arg3='3000', arg4='0')
        self.create_monster(spawnIds=[701], animationEffect=True) # 악당Mob_1
        self.create_monster(spawnIds=[702], animationEffect=True) # 악당Mob_2
        self.create_monster(spawnIds=[703], animationEffect=True) # 악당Mob_3
        self.create_monster(spawnIds=[704], animationEffect=True) # 악당Mob_4
        self.create_monster(spawnIds=[705], animationEffect=True) # 악당Mob_5
        self.create_monster(spawnIds=[706], animationEffect=True) # 악당Mob_6
        self.add_balloon_talk(spawnId=701, msg='$52010027_QD__MAIN__26$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=703, msg='$52010027_QD__MAIN__27$', duration=2000, delayTick=500)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[701,702,703,704,705,706]):
            return 연출_잠시쉬기_01(self.ctx)


class 연출_잠시쉬기_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출_페리온영웅등장(self.ctx)


class 연출_페리온영웅등장(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=2001, type='trigger', achieve='Windvalley')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.set_npc_emotion_loop(spawnId=501, sequenceName='Attack_Idle_A', duration=16000)
        self.set_scene_skip(state=페리온으로, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출_페리온영웅등장_보스대사(self.ctx)


class 연출_페리온영웅등장_보스대사(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__28$', duration=3000)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__29$', duration=3000)
        self.destroy_monster(spawnIds=[601])
        self.destroy_monster(spawnIds=[602])
        self.destroy_monster(spawnIds=[603])
        self.destroy_monster(spawnIds=[604])
        self.destroy_monster(spawnIds=[605])
        self.destroy_monster(spawnIds=[606])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 연출_페리온영웅등장_보스대사_02(self.ctx)


class 연출_페리온영웅등장_보스대사_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004,4015], returnView=False)
        self.add_balloon_talk(spawnId=501, msg='$52010027_QD__MAIN__30$', duration=2000, delayTick=0)
        self.add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__31$', duration=3000)
        self.add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__32$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 연출_페리온영웅등장_보스대사_03(self.ctx)


class 연출_페리온영웅등장_보스대사_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.add_balloon_talk(spawnId=501, msg='$52010027_QD__MAIN__33$', duration=2000, delayTick=0)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__34$', duration=3000)
        self.create_monster(spawnIds=[201], animationEffect=True) # 에바고르: 11003391
        self.create_monster(spawnIds=[101], animationEffect=True) # 시끄러운 주먹: 11003388

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return 연출_페리온영웅등장_02(self.ctx)


class 연출_페리온영웅등장_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.select_camera_path(pathIds=[4015,4006], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.show_caption(type='VerticalCaption', title='$52010027_QD__MAIN__35$', desc='$52010027_QD__MAIN__36$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        self.add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__37$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출_페리온영웅등장_03(self.ctx)


class 연출_페리온영웅등장_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__38$', duration=3000)
        self.add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__39$', duration=3000)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3002')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 연출_페리온영웅등장_04(self.ctx)


class 연출_페리온영웅등장_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__40$', duration=3000)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__41$', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 연출_페리온영웅등장_05(self.ctx)


class 연출_페리온영웅등장_05(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)
        self.destroy_monster(spawnIds=[501])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출_페리온영웅과대화(self.ctx)


class 연출_페리온영웅과대화(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Bore_B', duration=3000)
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Attack_Idle_A', duration=3000)
        self.add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__42$', duration=3500)
        self.add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__43$', duration=2000)
        self.add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__44$', duration=3500)
        self.move_user(mapId=52010027, portalId=6002)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 연출_페리온영웅과대화_02(self.ctx)


class 연출_페리온영웅과대화_02(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=201, emotionName='Trigger_NotAgree')
        self.select_camera_path(pathIds=[4010], returnView=False)
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=29000)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__45$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출_페리온영웅과대화_03(self.ctx)


class 연출_페리온영웅과대화_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.face_emotion(spawnId=201, emotionName='Trigger_NotAgree')
        self.add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__46$', duration=3000)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__47$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 연출_페리온영웅과대화_04(self.ctx)


class 연출_페리온영웅과대화_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4010], returnView=False)
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=29000)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__48$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__49$', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 연출_페리온영웅과대화_05(self.ctx)


class 연출_페리온영웅과대화_05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=15000)
        self.face_emotion(spawnId=201, emotionName='Trigger_Sad')
        self.add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__50$', duration=3000)
        self.add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__51$', duration=3000)
        self.add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__52$', duration=2000)
        self.add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__53$', duration=2000)
        self.add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__54$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=13000):
            return 연출_페리온영웅과대화_05_1(self.ctx)


class 연출_페리온영웅과대화_05_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 페리온으로(self.ctx)


class 페리온으로(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_portal(portalId=6003, visible=True, enable=True, minimapVisible=True)
        self.move_user(mapId=52010027, portalId=6004)
        self.destroy_monster(spawnIds=[201]) # 에바고르: 11003391
        self.destroy_monster(spawnIds=[101]) # 시끄러운 주먹: 11003388

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 페리온으로02(self.ctx)


class 페리온으로02(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 페리온으로03(self.ctx)


class 페리온으로03(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52010027_QD__MAIN__55$', arg3='3000', arg4='0')


initial_state = idle
