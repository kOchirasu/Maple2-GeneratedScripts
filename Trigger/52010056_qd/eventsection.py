""" trigger/52010056_qd/eventsection.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[9005], visible=True)
        self.set_mesh_animation(triggerIds=[9005], visible=True, arg3=0, arg4=0)
        self.set_mesh(triggerIds=[9006], visible=False)
        self.set_mesh_animation(triggerIds=[9006], visible=False, arg3=0, arg4=0)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False) # 포탈 생성
        self.set_effect(triggerIds=[5006], visible=False) # 포탈 생성
        self.set_effect(triggerIds=[5007], visible=False) # 포탈 생성
        self.set_effect(triggerIds=[5008], visible=False) # 포탈 사운드
        self.set_effect(triggerIds=[5009], visible=False) # 포탈 사운드
        self.set_effect(triggerIds=[5010], visible=False) # 포탈 사운드
        self.set_effect(triggerIds=[5011], visible=False) # 몸체 이펙트
        self.set_effect(triggerIds=[5012], visible=False) # 몸체 이펙트
        self.set_effect(triggerIds=[5013], visible=False) # 포탈 사운드
        self.set_effect(triggerIds=[5014], visible=False) # 트리스탄 바닥이펙트
        self.set_effect(triggerIds=[5101], visible=False)
        self.set_effect(triggerIds=[5102], visible=False)
        self.set_effect(triggerIds=[5103], visible=False)
        self.set_effect(triggerIds=[5104], visible=False)
        self.set_effect(triggerIds=[5105], visible=False)
        self.set_effect(triggerIds=[5106], visible=False)
        self.set_effect(triggerIds=[5107], visible=False)
        self.set_effect(triggerIds=[5108], visible=False)
        self.set_effect(triggerIds=[5109], visible=False)
        self.set_effect(triggerIds=[5110], visible=False)
        self.set_effect(triggerIds=[5111], visible=False)
        self.set_effect(triggerIds=[5112], visible=False)
        self.set_effect(triggerIds=[5113], visible=False)
        self.set_effect(triggerIds=[5114], visible=False)
        self.set_effect(triggerIds=[5115], visible=False)
        self.set_effect(triggerIds=[5116], visible=False)
        self.set_effect(triggerIds=[5117], visible=False)
        self.set_effect(triggerIds=[5118], visible=False)
        self.set_effect(triggerIds=[5201], visible=False)
        self.set_effect(triggerIds=[5202], visible=False)
        self.set_effect(triggerIds=[5203], visible=False)
        self.set_effect(triggerIds=[5204], visible=False)
        self.set_effect(triggerIds=[5205], visible=False)
        self.set_effect(triggerIds=[5206], visible=False)
        self.set_effect(triggerIds=[5207], visible=False)
        self.set_effect(triggerIds=[5208], visible=False)
        self.set_effect(triggerIds=[5209], visible=False)
        self.set_effect(triggerIds=[5210], visible=False)
        self.set_effect(triggerIds=[5211], visible=False)
        self.set_effect(triggerIds=[5212], visible=False)
        self.set_effect(triggerIds=[5213], visible=False)
        self.set_effect(triggerIds=[5214], visible=False)
        self.set_effect(triggerIds=[5215], visible=False)
        self.set_effect(triggerIds=[5216], visible=False)
        self.set_effect(triggerIds=[5218], visible=False)
        self.set_effect(triggerIds=[5218], visible=False)
        self.set_effect(triggerIds=[5301], visible=False)
        self.set_effect(triggerIds=[5302], visible=False)
        self.set_effect(triggerIds=[5303], visible=False)
        self.set_effect(triggerIds=[5304], visible=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml') # 페이드 아웃 끔

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=False) # 유저 투명화
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.create_monster(spawnIds=[111], animationEffect=False) # 보초1
        self.create_monster(spawnIds=[112], animationEffect=False) # 보초2
        self.create_monster(spawnIds=[121], animationEffect=False) # 크림슨 발록: 11003817
        self.create_monster(spawnIds=[122], animationEffect=False) # 크림슨 스피어 참모: 11003816
        self.create_monster(spawnIds=[123], animationEffect=False) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[124], animationEffect=False) # 크림슨 스피어2: 11003816
        self.create_monster(spawnIds=[125], animationEffect=False) # 크림슨 스피어3: 11003816
        self.create_monster(spawnIds=[126], animationEffect=False) # 크림슨 스피어4: 11003816
        self.create_monster(spawnIds=[191], animationEffect=False) # 인페르녹의 혼
        self.move_user(mapId=52010056, portalId=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 인트로_준비(self.ctx)


class 인트로_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52010056_QD__EventSection__52$', arg3=False)
        self.select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[2]):
            return 연출종료(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[1]):
            return 의외의효능_화면끔(self.ctx)
        if self.wait_tick(waitTick=4000):
            return 인트로_지역소개(self.ctx)


class 인트로_지역소개(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.show_caption(type='VerticalCaption', title='$52010056_QD__EventSection__54$', desc='$52010056_QD__EventSection__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3500, scale=1)
        self.set_scene_skip(state=시작연출_준비, action='nextState') # 크림슨 발록 연출 스킵
        # 트리스탄 등장 연출로 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 크림슨스피어_대사_A(self.ctx)


class 크림슨스피어_대사_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=126, patrolName='MS2PatrolData_3001')
        self.add_cinematic_talk(npcId=11003816, msg='$52010056_QD__EventSection__1$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크림슨발록_대사_A(self.ctx)


class 크림슨발록_대사_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=121, sequenceName='Stun_A')
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__2$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크림슨발록_대사_B(self.ctx)


class 크림슨발록_대사_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__3$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크림슨발록_대사_C(self.ctx)


class 크림슨발록_대사_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__4$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크림슨발록_대사_D(self.ctx)


class 크림슨발록_대사_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__5$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크림슨발록_대사_E(self.ctx)


class 크림슨발록_대사_E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__6$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크림슨발록_대사_F(self.ctx)


class 크림슨발록_대사_F(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__7$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 크림슨스피어_대사_B(self.ctx)

    def on_exit(self) -> None:
        self.set_npc_emotion_sequence(spawnId=121, sequenceName='Attack_01_C')


class 크림슨스피어_대사_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=125, patrolName='MS2PatrolData_3002')
        self.move_npc(spawnId=124, patrolName='MS2PatrolData_3003')
        self.move_npc(spawnId=123, patrolName='MS2PatrolData_3004')
        self.add_balloon_talk(spawnId=123, msg='$52010056_QD__EventSection__8$', duration=2800, delayTick=0)
        self.add_balloon_talk(spawnId=124, msg='$52010056_QD__EventSection__8$', duration=2800, delayTick=0)
        self.add_balloon_talk(spawnId=125, msg='$52010056_QD__EventSection__8$', duration=2800, delayTick=0)
        self.add_balloon_talk(spawnId=126, msg='$52010056_QD__EventSection__8$', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인트로_종료(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # 페이드 아웃 켬


class 인트로_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        # Missing State: State
        self.set_scene_skip() # 스킵 기능 끊어주기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 시작연출_준비(self.ctx)


class 시작연출_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52010056_QD__EventSection__53$', arg3=False)
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.create_monster(spawnIds=[101], animationEffect=False) # 트리스탄: 11003812

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 시작연출_지역소개(self.ctx)


class 시작연출_지역소개(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.show_caption(type='VerticalCaption', title='$52010056_QD__EventSection__12$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3500, scale=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 트리스탄_침입(self.ctx)


class 트리스탄_침입(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_3005')
        self.move_npc(spawnId=112, patrolName='MS2PatrolData_3006')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3007')
        self.add_balloon_talk(spawnId=111, msg='$52010056_QD__EventSection__13$', duration=2800, delayTick=0)
        self.add_balloon_talk(spawnId=112, msg='$52010056_QD__EventSection__14$', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 트리스탄_공격(self.ctx)


class 트리스탄_공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_effect(triggerIds=[5003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2100):
            return 트리스탄_마무리(self.ctx)


class 트리스탄_마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.set_effect(triggerIds=[5004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보초_쓰러짐(self.ctx)


class 보초_쓰러짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Dead_B', duration=1E+09)
        self.set_npc_emotion_loop(spawnId=112, sequenceName='Dead_B', duration=1E+09)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄_대사A(self.ctx)


class 트리스탄_대사A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__15$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄_대사B(self.ctx)


class 트리스탄_대사B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__16$', duration=2800, illustId='Tristan_normal', align='Center')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 조작_준비(self.ctx)


class 조작_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101]) # 트리스탄
        self.destroy_monster(spawnIds=[111]) # 보초1
        self.destroy_monster(spawnIds=[112]) # 보초2
        self.destroy_monster(spawnIds=[121]) # 크림슨 발록: 11003817
        self.destroy_monster(spawnIds=[122]) # 크림슨 참모: 11003816
        self.destroy_monster(spawnIds=[123]) # 크림슨 스피어1: 11003816
        self.destroy_monster(spawnIds=[124]) # 크림슨 스피어2: 11003816
        self.destroy_monster(spawnIds=[125]) # 크림슨 스피어3: 11003816
        self.destroy_monster(spawnIds=[126]) # 크림슨 스피어4: 11003816
        self.reset_camera(interpolationTime=1)
        self.visible_my_pc(isVisible=True) # 유저 투명 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 조작_시작(self.ctx)


class 조작_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_event_ui(type=1, arg2='$52010056_QD__EventSection__17$', arg3='3000', arg4='0')
        self.set_quest_accept(questId=91000053)
        self.set_visible_ui(uiNames=['UpperHudDialog','MessengerBrowser','ExpBar','GroupMessengerBrowser','QuestGuideDialog','MinimapDialog','AdPushDialog','SnowmanEventDialog'], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2010], questIds=[91000054], questStates=[2]):
            return 의외의효능_화면끔(self.ctx)
        if self.quest_user_detected(boxIds=[2010], questIds=[91000054], questStates=[1]):
            return 의외의효능_화면끔(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_sound(triggerId=7001, enable=False)


# 여기서부터 각성 연출
class 의외의효능_화면끔(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 의외의효능_준비(self.ctx)

    def on_exit(self) -> None:
        self.visible_my_pc(isVisible=False)
        # 유저 투명화
        self.create_monster(spawnIds=[102], animationEffect=False)
        # 트리스탄: 11003812
        self.destroy_monster(spawnIds=[111])
        self.destroy_monster(spawnIds=[112])
        self.destroy_monster(spawnIds=[121])
        self.destroy_monster(spawnIds=[122])
        self.destroy_monster(spawnIds=[123])
        self.destroy_monster(spawnIds=[124])
        self.destroy_monster(spawnIds=[125])
        self.destroy_monster(spawnIds=[126])


class 의외의효능_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(boxId=2001, skillId=99910300)
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.move_user(mapId=52010056, portalId=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 의외의효능_연출A(self.ctx)


class 의외의효능_연출A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__18$', duration=4569)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4569):
            return 의외의효능_연출B(self.ctx)


class 의외의효능_연출B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5005], visible=True)
        self.set_effect(triggerIds=[5008], visible=True)
        self.create_monster(spawnIds=[801], animationEffect=False) # 크림슨 스피어1: 11003816
        self.select_camera_path(pathIds=[4009,4010], returnView=False)
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__19$', duration=2800)
        self.set_scene_skip(state=각성_전투준비, action='nextState') # 트리스탄 각성 전투로 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5008], visible=False)
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__20$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 크림슨군단생성(self.ctx)


class 크림슨군단생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5006], visible=True)
        self.set_effect(triggerIds=[5007], visible=True)
        self.set_effect(triggerIds=[5009], visible=True)
        self.set_effect(triggerIds=[5010], visible=True)
        self.set_effect(triggerIds=[5012], visible=True)
        self.set_effect(triggerIds=[5013], visible=True)
        self.create_monster(spawnIds=[802], animationEffect=False) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[803], animationEffect=False) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[804], animationEffect=False) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[805], animationEffect=False) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[806], animationEffect=False) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[807], animationEffect=False) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 크림슨군단진영(self.ctx)


class 크림슨군단진영(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5006], visible=False)
        self.set_effect(triggerIds=[5007], visible=False)
        self.set_effect(triggerIds=[5009], visible=False)
        self.set_effect(triggerIds=[5010], visible=False)
        self.set_effect(triggerIds=[5012], visible=False)
        self.set_effect(triggerIds=[5013], visible=False)
        self.set_npc_emotion_sequence(spawnId=801, sequenceName='Stun_A')
        self.move_npc(spawnId=802, patrolName='MS2PatrolData_3009')
        self.move_npc(spawnId=803, patrolName='MS2PatrolData_3010')
        self.move_npc(spawnId=804, patrolName='MS2PatrolData_3011')
        self.move_npc(spawnId=805, patrolName='MS2PatrolData_3012')
        self.move_npc(spawnId=806, patrolName='MS2PatrolData_3013')
        self.move_npc(spawnId=807, patrolName='MS2PatrolData_3014')
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__21$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 크림슨발록분노(self.ctx)


class 크림슨발록분노(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=801, sequenceName='Attack_01_B')
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__22$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄대사_A(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # 페이드 아웃 켬


class 트리스탄대사_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__23$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄대사_B(self.ctx)


class 트리스탄대사_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__24$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크림슨발록대사_A(self.ctx)


class 크림슨발록대사_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4011], returnView=False)
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__25$', duration=2800, illustId='balrog_normal', align='Center')
        self.set_effect(triggerIds=[5011], visible=True) # 몸체 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_A(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # 페이드 아웃 끔


class 인페르녹의혼_흡수연출_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Attack_02_B', duration=1E+09)
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__26$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_B(self.ctx)


class 인페르녹의혼_흡수연출_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4012], returnView=False)
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__27$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_C(self.ctx)


class 인페르녹의혼_흡수연출_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5012], visible=True) # 몸체 이펙트
        self.set_effect(triggerIds=[5013], visible=True) # 펑
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__28$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 인페르녹의혼_흡수연출_D(self.ctx)


class 인페르녹의혼_흡수연출_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 인페르녹의혼_흡수연출_E(self.ctx)


class 인페르녹의혼_흡수연출_E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__29$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_F(self.ctx)


class 인페르녹의혼_흡수연출_F(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__30$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_G(self.ctx)


class 인페르녹의혼_흡수연출_G(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__31$', duration=2800, align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_H(self.ctx)


class 인페르녹의혼_흡수연출_H(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__32$', duration=2800, align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_I(self.ctx)


class 인페르녹의혼_흡수연출_I(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__33$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_J(self.ctx)


class 인페르녹의혼_흡수연출_J(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__34$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_K(self.ctx)


class 인페르녹의혼_흡수연출_K(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__35$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_L(self.ctx)


class 인페르녹의혼_흡수연출_L(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__36$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_M(self.ctx)


class 인페르녹의혼_흡수연출_M(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__37$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_N(self.ctx)


class 인페르녹의혼_흡수연출_N(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4013], returnView=False)
        self.add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__38$', duration=2800)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 각성_전투준비(self.ctx)


class 각성_전투준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_mesh(triggerIds=[9005], visible=False)
        self.set_mesh_animation(triggerIds=[9005], visible=False, arg3=0, arg4=0)
        self.set_mesh(triggerIds=[9006], visible=True)
        self.set_mesh_animation(triggerIds=[9006], visible=True, arg3=0, arg4=0)
        self.destroy_monster(spawnIds=[102]) # 트리스탄
        self.destroy_monster(spawnIds=[802])
        self.destroy_monster(spawnIds=[803])
        self.destroy_monster(spawnIds=[804])
        self.destroy_monster(spawnIds=[805])
        self.destroy_monster(spawnIds=[806])
        self.destroy_monster(spawnIds=[807])
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)
        self.set_effect(triggerIds=[5007], visible=False)
        self.set_effect(triggerIds=[5008], visible=False)
        self.set_effect(triggerIds=[5009], visible=False)
        self.set_effect(triggerIds=[5010], visible=False)
        self.set_effect(triggerIds=[5009], visible=False)
        self.set_effect(triggerIds=[5010], visible=False)
        self.set_effect(triggerIds=[5011], visible=False)
        self.set_effect(triggerIds=[5012], visible=False)
        self.set_effect(triggerIds=[5013], visible=False)
        self.visible_my_pc(isVisible=True) # 유저 투명 해제
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 각성_전투시작(self.ctx)


class 각성_전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__39$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 조작제어_해제(self.ctx)


class 조작제어_해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 크림슨발록군단생성_A(self.ctx)


class 크림슨발록군단생성_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[701], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[702], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[703], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[704], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[705], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[706], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[707], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[708], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[709], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[710], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[711], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[712], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[713], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[714], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[715], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[716], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[717], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[718], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[719], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[720], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[721], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[722], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[723], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[724], animationEffect=True) # 크림슨 스피어1: 11003816
        self.set_event_ui(type=1, arg2='$52010056_QD__EventSection__40$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크림슨발록군단생성_B(self.ctx)


class 크림슨발록군단생성_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[701], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[702], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[703], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[704], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[705], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[706], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[707], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[708], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[709], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[710], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[711], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[712], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[713], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[714], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[715], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[716], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[717], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[718], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[719], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[720], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[721], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[722], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[723], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[724], animationEffect=True) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크림슨발록군단생성_C(self.ctx)


class 크림슨발록군단생성_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[701], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[702], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[703], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[704], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[705], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[706], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[707], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[708], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[709], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[710], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[711], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[712], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[713], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[714], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[715], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[716], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[717], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[718], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[719], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[720], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[721], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[722], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[723], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[724], animationEffect=True) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 크림슨발록군단생성_D(self.ctx)


class 크림슨발록군단생성_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[701], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[702], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[703], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[704], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[705], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[706], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[707], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[708], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[709], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[710], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[711], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[712], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[713], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[714], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[715], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[716], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[717], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[718], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[719], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[720], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[721], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[722], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[723], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[724], animationEffect=True) # 크림슨 스피어1: 11003816
        self.set_event_ui(type=1, arg2='$52010056_QD__EventSection__41$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 크림슨발록군단생성_E(self.ctx)


class 크림슨발록군단생성_E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[701], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[702], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[703], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[704], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[705], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[706], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[707], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[708], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[709], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[710], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[711], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[712], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[713], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[714], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[715], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[716], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[717], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[718], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[719], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[720], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[721], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[722], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[723], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[724], animationEffect=True) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 크림슨발록군단생성_F(self.ctx)


class 크림슨발록군단생성_F(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[701], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[702], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[703], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[704], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[705], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[706], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[707], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[708], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[709], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[710], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[711], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[712], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[713], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[714], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[715], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[716], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[717], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[718], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[719], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[720], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[721], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[722], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[723], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[724], animationEffect=True) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724]):
            return 필살기연출_암전(self.ctx)


class 필살기연출_암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=False) # 유저 투명
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬
        self.move_user(mapId=52010056, portalId=6003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 필살기연출_준비A(self.ctx)


class 필살기연출_준비A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[701])
        self.destroy_monster(spawnIds=[702])
        self.destroy_monster(spawnIds=[703])
        self.destroy_monster(spawnIds=[704])
        self.destroy_monster(spawnIds=[705])
        self.destroy_monster(spawnIds=[706])
        self.destroy_monster(spawnIds=[707])
        self.destroy_monster(spawnIds=[708])
        self.destroy_monster(spawnIds=[709])
        self.destroy_monster(spawnIds=[710])
        self.destroy_monster(spawnIds=[711])
        self.destroy_monster(spawnIds=[712])
        self.destroy_monster(spawnIds=[713])
        self.destroy_monster(spawnIds=[714])
        self.destroy_monster(spawnIds=[715])
        self.destroy_monster(spawnIds=[716])
        self.destroy_monster(spawnIds=[717])
        self.destroy_monster(spawnIds=[718])
        self.destroy_monster(spawnIds=[719])
        self.destroy_monster(spawnIds=[720])
        self.destroy_monster(spawnIds=[721])
        self.destroy_monster(spawnIds=[722])
        self.destroy_monster(spawnIds=[723])
        self.destroy_monster(spawnIds=[724])
        self.create_monster(spawnIds=[103], animationEffect=True) # 트리스탄
        self.create_monster(spawnIds=[808], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[809], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[810], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[811], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[812], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[813], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[814], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[815], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[816], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[817], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[818], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[819], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[820], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[821], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[822], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[823], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[824], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[825], animationEffect=True) # 크림슨 스피어1: 11003816
        self.create_monster(spawnIds=[826], animationEffect=True) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 필살기연출_준비B(self.ctx)


class 필살기연출_준비B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=808, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=809, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=810, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=811, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=812, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=813, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=814, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=815, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=816, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=817, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=818, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=819, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=820, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=821, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=822, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=823, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=824, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=825, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=826, sequenceName='Attack_Idle_A', duration=9999999)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 카메라_온A(self.ctx)


class 카메라_온A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.select_camera_path(pathIds=[4014], returnView=False)
        self.set_scene_skip(state=트리거업적, action='nextState') # 크림슨 발록 연출 스킵
        # 트리스탄 등장 연출로 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 카메라_온B(self.ctx)


class 카메라_온B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4015], returnView=False)
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__42$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 카메라_온C(self.ctx)


class 카메라_온C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4016], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 카메라_리셋(self.ctx)


class 카메라_리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 크림슨발록_대사_G(self.ctx)


class 크림슨발록_대사_G(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=801, sequenceName='Attack_01_B')
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__43$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄_대사_H(self.ctx)


class 트리스탄_대사_H(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__44$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크림슨발록_대사_I(self.ctx)


class 크림슨발록_대사_I(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__45$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄_대사D(self.ctx)


class 트리스탄_대사D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__46$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄_대사E(self.ctx)


class 트리스탄_대사E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__47$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 필살기연출_모션A(self.ctx)


class 필살기연출_모션A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Attack_02_B', duration=9999999)
        self.set_effect(triggerIds=[5014], visible=True) # 트리스탄 바닥이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 필살기연출_모션B(self.ctx)


class 필살기연출_모션B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Attack_01_B', duration=9999999)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 크림슨발록_대사_J(self.ctx)


class 크림슨발록_대사_J(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__48$', duration=1800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1800):
            return 크림슨발록_대사_K(self.ctx)


class 크림슨발록_대사_K(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5101], visible=True) # 트리스탄 바닥이펙트
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__55$', duration=1800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_A(self.ctx)


class 바닥이펙트_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=808, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5102], visible=True)
        self.set_effect(triggerIds=[5202], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_B(self.ctx)


class 바닥이펙트_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=809, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5103], visible=True)
        self.set_effect(triggerIds=[5203], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_C(self.ctx)


class 바닥이펙트_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=810, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5104], visible=True)
        self.set_effect(triggerIds=[5204], visible=True)
        self.set_effect(triggerIds=[5302], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_D(self.ctx)


class 바닥이펙트_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=811, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5105], visible=True)
        self.set_effect(triggerIds=[5205], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_E(self.ctx)


class 바닥이펙트_E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=812, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5106], visible=True)
        self.set_effect(triggerIds=[5206], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_F(self.ctx)


class 바닥이펙트_F(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=813, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5107], visible=True)
        self.set_effect(triggerIds=[5207], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_G(self.ctx)


class 바닥이펙트_G(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=814, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5108], visible=True)
        self.set_effect(triggerIds=[5208], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_H(self.ctx)


class 바닥이펙트_H(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=815, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5109], visible=True)
        self.set_effect(triggerIds=[5209], visible=True)
        self.set_effect(triggerIds=[5303], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_I(self.ctx)


class 바닥이펙트_I(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=816, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5110], visible=True)
        self.set_effect(triggerIds=[5210], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_J(self.ctx)


class 바닥이펙트_J(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=817, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5111], visible=True)
        self.set_effect(triggerIds=[5211], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_K(self.ctx)


class 바닥이펙트_K(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=818, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5112], visible=True)
        self.set_effect(triggerIds=[5212], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_L(self.ctx)


class 바닥이펙트_L(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=819, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5113], visible=True)
        self.set_effect(triggerIds=[5213], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_M(self.ctx)


class 바닥이펙트_M(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=820, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5114], visible=True)
        self.set_effect(triggerIds=[5214], visible=True)
        self.set_effect(triggerIds=[5304], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_N(self.ctx)


class 바닥이펙트_N(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=821, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5115], visible=True)
        self.set_effect(triggerIds=[5215], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_O(self.ctx)


class 바닥이펙트_O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=822, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5116], visible=True)
        self.set_effect(triggerIds=[5216], visible=True)
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml') # 페이드 아웃 켬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_P(self.ctx)


class 바닥이펙트_P(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=823, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5117], visible=True)
        self.set_effect(triggerIds=[5217], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_Q(self.ctx)


class 바닥이펙트_Q(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=824, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5118], visible=True)
        self.set_effect(triggerIds=[5218], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 바닥이펙트_R(self.ctx)


class 바닥이펙트_R(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=825, sequenceName='Damg_A', duration=9999999)
        self.set_effect(triggerIds=[5202], visible=True)
        self.set_effect(triggerIds=[5301], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크림슨발록_대사_L(self.ctx)


class 크림슨발록_대사_L(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__50$', duration=2800, illustId='balrog_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마지막연출_세팅(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[103])
        self.create_monster(spawnIds=[104], animationEffect=True)
        # 트리스탄


class 마지막연출_세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5101], visible=False)
        self.set_effect(triggerIds=[5102], visible=False)
        self.set_effect(triggerIds=[5103], visible=False)
        self.set_effect(triggerIds=[5104], visible=False)
        self.set_effect(triggerIds=[5105], visible=False)
        self.set_effect(triggerIds=[5106], visible=False)
        self.set_effect(triggerIds=[5107], visible=False)
        self.set_effect(triggerIds=[5108], visible=False)
        self.set_effect(triggerIds=[5109], visible=False)
        self.set_effect(triggerIds=[5110], visible=False)
        self.set_effect(triggerIds=[5111], visible=False)
        self.set_effect(triggerIds=[5112], visible=False)
        self.set_effect(triggerIds=[5113], visible=False)
        self.set_effect(triggerIds=[5114], visible=False)
        self.set_effect(triggerIds=[5115], visible=False)
        self.set_effect(triggerIds=[5116], visible=False)
        self.set_effect(triggerIds=[5117], visible=False)
        self.set_effect(triggerIds=[5118], visible=False)
        self.set_effect(triggerIds=[5201], visible=False)
        self.set_effect(triggerIds=[5202], visible=False)
        self.set_effect(triggerIds=[5203], visible=False)
        self.set_effect(triggerIds=[5204], visible=False)
        self.set_effect(triggerIds=[5205], visible=False)
        self.set_effect(triggerIds=[5206], visible=False)
        self.set_effect(triggerIds=[5207], visible=False)
        self.set_effect(triggerIds=[5208], visible=False)
        self.set_effect(triggerIds=[5209], visible=False)
        self.set_effect(triggerIds=[5210], visible=False)
        self.set_effect(triggerIds=[5211], visible=False)
        self.set_effect(triggerIds=[5212], visible=False)
        self.set_effect(triggerIds=[5213], visible=False)
        self.set_effect(triggerIds=[5214], visible=False)
        self.set_effect(triggerIds=[5215], visible=False)
        self.set_effect(triggerIds=[5216], visible=False)
        self.set_effect(triggerIds=[5218], visible=False)
        self.set_effect(triggerIds=[5218], visible=False)
        self.set_effect(triggerIds=[5301], visible=False)
        self.set_effect(triggerIds=[5302], visible=False)
        self.set_effect(triggerIds=[5303], visible=False)
        self.set_effect(triggerIds=[5304], visible=False)
        self.reset_camera(interpolationTime=0)
        self.set_npc_emotion_loop(spawnId=104, sequenceName='Attack_Idle_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=801, sequenceName='Dead_01_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=808, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=809, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=810, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=811, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=812, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=813, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=814, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=815, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=816, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=817, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=818, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=819, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=820, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=821, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=822, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=823, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=824, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=825, sequenceName='Dead_A', duration=9999999)
        self.set_npc_emotion_loop(spawnId=826, sequenceName='Dead_A', duration=9999999)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마지막연출_온(self.ctx)


class 마지막연출_온(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml') # 페이드 아웃 켬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리스탄_대사F(self.ctx)


class 트리스탄_대사F(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__51$', duration=2800, illustId='Tristan_normal', align='Center')
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리거업적(self.ctx)


class 트리거업적(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=2009, type='trigger', achieve='tristanarousal')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52010052, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[2]):
            return 연출종료(self.ctx)


initial_state = Idle
