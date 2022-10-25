""" trigger/52000112_qd/52000112.xml """
import common


class START(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5300], visible=False) # 재즈바 비밀통로 경로 안내
        self.create_monster(spawnIds=[101], animationEffect=False) # 바텐더
        self.set_actor(triggerId=231, visible=True, initialSequence='Closed')
        self.set_effect(triggerIds=[400], visible=False)
        self.set_effect(triggerIds=[401], visible=False)
        self.set_effect(triggerIds=[402], visible=False)
        self.set_effect(triggerIds=[403], visible=False)
        self.set_effect(triggerIds=[404], visible=False)
        self.set_effect(triggerIds=[405], visible=False)
        self.set_effect(triggerIds=[406], visible=False)
        self.set_effect(triggerIds=[407], visible=False)
        self.set_mesh(triggerIds=[300,301,302,303,304,305,306,307], visible=True, arg3=0, delay=1000, scale=1000) # 큐브하나씩부셔지는연출

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002306], questStates=[2]):
            return 재즈바1층습격_완료가능01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002306], questStates=[1]):
            return 재즈바1층습격_진행중01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002308], questStates=[2]):
            return 재즈바_지하습격_완료가능01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[2]):
            return 쉐도우클로전투_완료연출01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002311], questStates=[3]):
            return 재즈바_지하습격_완료가능01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002308], questStates=[3]):
            return 재즈바_지하습격_완료가능01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002306], questStates=[3]):
            return 재즈바1층습격_완료가능01(self.ctx)


# ########################씬1 재즈바_1층습격########################
class 재즈바1층습격_진행중01(common.Trigger):
    def on_enter(self):
        self.spawn_npc_range(rangeIds=[102,103,104,105,106,107], isAutoTargeting=True)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002306], questStates=[2]):
            return 재즈바1층습격_완료가능01_b(self.ctx)


class 재즈바1층습격_완료가능01_b(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$52000112_QD__52000112__0$', duration=6000, delayTick=1000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 재즈바1층습격_완료가능01(self.ctx)


class 재즈바1층습격_완료가능01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 재즈바1층습격_완료가능02(self.ctx)


class 재즈바1층습격_완료가능02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[200], animationEffect=False)
        self.destroy_monster(spawnIds=[102,103,104,105,106,107])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 재즈바1층습격_완료가능03(self.ctx)


class 재즈바1층습격_완료가능03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_shadowClawMove') # 쉐도우클로 이동
        self.add_balloon_talk(spawnId=111, msg='$52000112_QD__52000112__1$', duration=6000, delayTick=1000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002308], questStates=[1]):
            return 재즈바_지하습격_진행중01(self.ctx)


# ########################씬2 재즈바_지하습격########################
class 재즈바_지하습격_진행중01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5300], visible=True) # 재즈바 비밀통로 경로 안내
        self.set_actor(triggerId=231, visible=True, initialSequence='Opened')
        self.create_monster(spawnIds=[200,209,204,205,210,206], animationEffect=False) # 지하층 다크윈드 요원 생성

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002308], questStates=[2]):
            return 재즈바_지하습격_완료가능01_b(self.ctx)


class 재즈바_지하습격_완료가능01_b(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$52000112_QD__52000112__2$', duration=6000, delayTick=1000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 재즈바_지하습격_완료가능01(self.ctx)


class 재즈바_지하습격_완료가능01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 재즈바_지하습격_완료가능02(self.ctx)


class 재즈바_지하습격_완료가능02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=20, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.create_monster(spawnIds=[208], animationEffect=False) # 쉐도우클로
        self.create_monster(spawnIds=[201,202,203], animationEffect=False) # 다크윈드 포로
        self.create_monster(spawnIds=[211,212,213,214,215,216,217,218,219], animationEffect=False) # 로그스 대원
        self.destroy_monster(spawnIds=[108,109,110,111,200,209,204,205,210,206])
        self.move_user(mapId=52000112, portalId=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 재즈바_지하습격_완료가능03(self.ctx)


class 재즈바_지하습격_완료가능03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002311], questStates=[3]):
            return PC_로그스거역_진행중01(self.ctx)


# ########################씬3 PC_로그스거역_대원들 전투준비########################
class PC_로그스거역_진행중01(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=211, sequenceName='Attack_Idle_A', duration=15000)
        self.set_npc_emotion_loop(spawnId=212, sequenceName='Attack_Idle_A', duration=15000)
        self.set_npc_emotion_loop(spawnId=213, sequenceName='Attack_Idle_A', duration=15000)
        self.set_npc_emotion_loop(spawnId=214, sequenceName='Attack_Idle_A', duration=15000)
        self.set_npc_emotion_loop(spawnId=215, sequenceName='Attack_Idle_A', duration=15000)
        self.set_npc_emotion_loop(spawnId=216, sequenceName='Attack_Idle_A', duration=15000)
        self.set_npc_emotion_loop(spawnId=217, sequenceName='Attack_Idle_A', duration=15000)
        self.set_npc_emotion_loop(spawnId=218, sequenceName='Attack_Idle_A', duration=15000)
        self.set_npc_emotion_loop(spawnId=219, sequenceName='Attack_Idle_A', duration=15000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002312], questStates=[3]):
            return PC_로그스거역_대원들01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002312], questStates=[2]):
            return PC_로그스거역_대원들01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002312], questStates=[1]):
            return PC_로그스거역_대원들01(self.ctx)


# ########################씬3 PC_로그스거역_대원들 전투########################
class PC_로그스거역_대원들01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[211,212,213,214,215,216,217,218,219]) # 로그스 대원 npc버전 삭제
        self.create_monster(spawnIds=[220,221,222,223,224,225,226,227,228], animationEffect=False) # 로그스 대원 몬스터 생성

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[1]):
            return 쉐도우클로전투_진행중01(self.ctx)


# ########################씬4 쉐도우클로전투########################
class 쉐도우클로전투_진행중01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[211,212,213,214,215,216,217,218,219]) # 로그스 대원 npc버전 삭제
        self.destroy_monster(spawnIds=[220,221,222,223,224,225,226,227,228]) # 로그스 대원 몬스터 삭제
        self.set_sound(triggerId=9000, enable=True)
        self.destroy_monster(spawnIds=[208])
        self.create_monster(spawnIds=[229], animationEffect=False) # 쉐도우클로

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[2]):
            return 쉐도우클로전투_완료연출01(self.ctx)


# ########################씬5 쉐도우클로전투_완료연출########################
class 쉐도우클로전투_완료연출01(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=9000, enable=False)
        self.visible_my_pc(isVisible=True) # 유저 투명 처리
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[207])
        self.create_monster(spawnIds=[208], animationEffect=False) # 쉐도우클로
        self.move_user(mapId=52000112, portalId=3)
        self.set_npc_emotion_loop(spawnId=208, sequenceName='Attack_Idle_A', duration=17500)
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Sit_Down_A', duration=17500)
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Sit_Down_A', duration=17500)
        self.set_npc_emotion_loop(spawnId=203, sequenceName='Sit_Down_A', duration=17500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 쉐도우클로전투_완료연출02(self.ctx)


class 쉐도우클로전투_완료연출02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=쉐도우클로전투_완료연출09, action='exit')
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.select_camera_path(pathIds=[3000,3001], returnView=False)
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=5000)
        self.face_emotion(spawnId=0, emotionName='PC_Pain_86000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 쉐도우클로전투_완료연출03(self.ctx)


class 쉐도우클로전투_완료연출03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3002,3003], returnView=False)
        self.add_cinematic_talk(npcId=11003185, illustId='0', msg='$52000112_QD__52000112__3$', duration=5000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 쉐도우클로전투_완료연출04(self.ctx)


class 쉐도우클로전투_완료연출04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000112_QD__52000112__4$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 쉐도우클로전투_완료연출05(self.ctx)


class 쉐도우클로전투_완료연출05(common.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=True, startScale=1, endScale=0.1, duration=5.5, interpolator=2) # 2초간 느려지기 시작
        self.select_camera_path(pathIds=[3004], returnView=False)
        self.set_pc_emotion_sequence(sequenceNames=['Assassin_DarkSight_A'])
        self.set_pc_emotion_loop(sequenceName='Assassin_DarkSight_A', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 쉐도우클로전투_완료연출06(self.ctx)


class 쉐도우클로전투_완료연출06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3005,3006], returnView=False)
        self.set_pc_emotion_sequence(sequenceNames=['Assassin_Enterance_A'])
        self.set_pc_emotion_loop(sequenceName='Assassin_Enterance_A', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 쉐도우클로전투_완료연출07_b(self.ctx)


class 쉐도우클로전투_완료연출07_b(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[400], visible=True)
        self.set_effect(triggerIds=[401], visible=True)
        self.set_effect(triggerIds=[402], visible=True)
        self.set_effect(triggerIds=[403], visible=True)
        self.set_effect(triggerIds=[404], visible=True)
        self.set_effect(triggerIds=[405], visible=True)
        self.set_effect(triggerIds=[406], visible=True)
        self.set_effect(triggerIds=[407], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1700):
            return 쉐도우클로전투_완료연출07(self.ctx)


class 쉐도우클로전투_완료연출07(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3007,3008], returnView=False)
        self.add_cinematic_talk(npcId=11003185, illustId='0', msg='$52000112_QD__52000112__5$', duration=4000, align='right')
        self.set_npc_emotion_loop(spawnId=208, sequenceName='Stun_A', duration=15500)
        self.set_mesh(triggerIds=[300,301,302,303,304,305,306,307], visible=False, arg3=0, delay=700, scale=0) # 큐브하나씩부셔지는연출

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 쉐도우클로전투_완료연출08(self.ctx)


class 쉐도우클로전투_완료연출08(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3009,3010], returnView=False)
        self.destroy_monster(spawnIds=[201,202,203])
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.add_cinematic_talk(npcId=11003185, illustId='0', msg='$52000112_QD__52000112__6$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 쉐도우클로전투_완료연출08_1(self.ctx)


class 쉐도우클로전투_완료연출08_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 쉐도우클로전투_완료연출09(self.ctx)


class 쉐도우클로전투_완료연출09(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000111, portalId=11)


initial_state = START
