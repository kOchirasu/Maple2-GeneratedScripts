""" trigger/52010056_qd/eventsection.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9005], visible=True)
        set_mesh_animation(triggerIds=[9005], visible=True, arg3=0, arg4=0)
        set_mesh(triggerIds=[9006], visible=False)
        set_mesh_animation(triggerIds=[9006], visible=False, arg3=0, arg4=0)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False) # 포탈 생성
        set_effect(triggerIds=[5006], visible=False) # 포탈 생성
        set_effect(triggerIds=[5007], visible=False) # 포탈 생성
        set_effect(triggerIds=[5008], visible=False) # 포탈 사운드
        set_effect(triggerIds=[5009], visible=False) # 포탈 사운드
        set_effect(triggerIds=[5010], visible=False) # 포탈 사운드
        set_effect(triggerIds=[5011], visible=False) # 몸체 이펙트
        set_effect(triggerIds=[5012], visible=False) # 몸체 이펙트
        set_effect(triggerIds=[5013], visible=False) # 포탈 사운드
        set_effect(triggerIds=[5014], visible=False) # 트리스탄 바닥이펙트
        set_effect(triggerIds=[5101], visible=False)
        set_effect(triggerIds=[5102], visible=False)
        set_effect(triggerIds=[5103], visible=False)
        set_effect(triggerIds=[5104], visible=False)
        set_effect(triggerIds=[5105], visible=False)
        set_effect(triggerIds=[5106], visible=False)
        set_effect(triggerIds=[5107], visible=False)
        set_effect(triggerIds=[5108], visible=False)
        set_effect(triggerIds=[5109], visible=False)
        set_effect(triggerIds=[5110], visible=False)
        set_effect(triggerIds=[5111], visible=False)
        set_effect(triggerIds=[5112], visible=False)
        set_effect(triggerIds=[5113], visible=False)
        set_effect(triggerIds=[5114], visible=False)
        set_effect(triggerIds=[5115], visible=False)
        set_effect(triggerIds=[5116], visible=False)
        set_effect(triggerIds=[5117], visible=False)
        set_effect(triggerIds=[5118], visible=False)
        set_effect(triggerIds=[5201], visible=False)
        set_effect(triggerIds=[5202], visible=False)
        set_effect(triggerIds=[5203], visible=False)
        set_effect(triggerIds=[5204], visible=False)
        set_effect(triggerIds=[5205], visible=False)
        set_effect(triggerIds=[5206], visible=False)
        set_effect(triggerIds=[5207], visible=False)
        set_effect(triggerIds=[5208], visible=False)
        set_effect(triggerIds=[5209], visible=False)
        set_effect(triggerIds=[5210], visible=False)
        set_effect(triggerIds=[5211], visible=False)
        set_effect(triggerIds=[5212], visible=False)
        set_effect(triggerIds=[5213], visible=False)
        set_effect(triggerIds=[5214], visible=False)
        set_effect(triggerIds=[5215], visible=False)
        set_effect(triggerIds=[5216], visible=False)
        set_effect(triggerIds=[5218], visible=False)
        set_effect(triggerIds=[5218], visible=False)
        set_effect(triggerIds=[5301], visible=False)
        set_effect(triggerIds=[5302], visible=False)
        set_effect(triggerIds=[5303], visible=False)
        set_effect(triggerIds=[5304], visible=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml') # 페이드 아웃 끔

    def on_tick(self) -> state.State:
        if true():
            return Ready()


class Ready(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False) # 유저 투명화
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        create_monster(spawnIds=[111], arg2=False) # 보초1
        create_monster(spawnIds=[112], arg2=False) # 보초2
        create_monster(spawnIds=[121], arg2=False) # 크림슨 발록: 11003817
        create_monster(spawnIds=[122], arg2=False) # 크림슨 스피어 참모: 11003816
        create_monster(spawnIds=[123], arg2=False) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[124], arg2=False) # 크림슨 스피어2: 11003816
        create_monster(spawnIds=[125], arg2=False) # 크림슨 스피어3: 11003816
        create_monster(spawnIds=[126], arg2=False) # 크림슨 스피어4: 11003816
        create_monster(spawnIds=[191], arg2=False) # 인페르녹의 혼
        move_user(mapId=52010056, portalId=6001)

    def on_tick(self) -> state.State:
        if true():
            return 인트로_준비()


class 인트로_준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52010056_QD__EventSection__52$', arg3=False)
        select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[2]):
            return 연출종료()
        if quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[1]):
            return 의외의효능_화면끔()
        if wait_tick(waitTick=4000):
            return 인트로_지역소개()


class 인트로_지역소개(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        show_caption(type='VerticalCaption', title='$52010056_QD__EventSection__54$', desc='$52010056_QD__EventSection__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3500, scale=1)
        set_scene_skip(state=시작연출_준비, arg2='nextState') # 크림슨 발록 연출 스킵

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 크림슨스피어_대사_A()


class 크림슨스피어_대사_A(state.State):
    def on_enter(self):
        move_npc(spawnId=126, patrolName='MS2PatrolData_3001')
        add_cinematic_talk(npcId=11003816, msg='$52010056_QD__EventSection__1$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크림슨발록_대사_A()


class 크림슨발록_대사_A(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=121, sequenceName='Stun_A')
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__2$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크림슨발록_대사_B()


class 크림슨발록_대사_B(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__3$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크림슨발록_대사_C()


class 크림슨발록_대사_C(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__4$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크림슨발록_대사_D()


class 크림슨발록_대사_D(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__5$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크림슨발록_대사_E()


class 크림슨발록_대사_E(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__6$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크림슨발록_대사_F()


class 크림슨발록_대사_F(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__7$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 크림슨스피어_대사_B()

    def on_exit(self):
        set_npc_emotion_sequence(spawnId=121, sequenceName='Attack_01_C')


class 크림슨스피어_대사_B(state.State):
    def on_enter(self):
        move_npc(spawnId=125, patrolName='MS2PatrolData_3002')
        move_npc(spawnId=124, patrolName='MS2PatrolData_3003')
        move_npc(spawnId=123, patrolName='MS2PatrolData_3004')
        add_balloon_talk(spawnId=123, msg='$52010056_QD__EventSection__8$', duration=2800, delayTick=0)
        add_balloon_talk(spawnId=124, msg='$52010056_QD__EventSection__8$', duration=2800, delayTick=0)
        add_balloon_talk(spawnId=125, msg='$52010056_QD__EventSection__8$', duration=2800, delayTick=0)
        add_balloon_talk(spawnId=126, msg='$52010056_QD__EventSection__8$', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인트로_종료()

    def on_exit(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬


class 인트로_종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_scene_skip() # 스킵 기능 끊어주기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 시작연출_준비()


class 시작연출_준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52010056_QD__EventSection__53$', arg3=False)
        select_camera_path(pathIds=[4002], returnView=False)
        create_monster(spawnIds=[101], arg2=False) # 트리스탄: 11003812

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 시작연출_지역소개()


class 시작연출_지역소개(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        show_caption(type='VerticalCaption', title='$52010056_QD__EventSection__12$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3500, scale=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 트리스탄_침입()


class 트리스탄_침입(state.State):
    def on_enter(self):
        move_npc(spawnId=111, patrolName='MS2PatrolData_3005')
        move_npc(spawnId=112, patrolName='MS2PatrolData_3006')
        move_npc(spawnId=101, patrolName='MS2PatrolData_3007')
        add_balloon_talk(spawnId=111, msg='$52010056_QD__EventSection__13$', duration=2800, delayTick=0)
        add_balloon_talk(spawnId=112, msg='$52010056_QD__EventSection__14$', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트리스탄_공격()


class 트리스탄_공격(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)
        set_effect(triggerIds=[5003], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2100):
            return 트리스탄_마무리()


class 트리스탄_마무리(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        set_effect(triggerIds=[5004], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보초_쓰러짐()


class 보초_쓰러짐(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=111, sequenceName='Dead_B', duration=1E+09)
        set_npc_emotion_loop(spawnId=112, sequenceName='Dead_B', duration=1E+09)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄_대사A()


class 트리스탄_대사A(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__15$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄_대사B()


class 트리스탄_대사B(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__16$', duration=2800, illustId='Tristan_normal', align='Center')
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 조작_준비()


class 조작_준비(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101]) # 트리스탄
        destroy_monster(spawnIds=[111]) # 보초1
        destroy_monster(spawnIds=[112]) # 보초2
        destroy_monster(spawnIds=[121]) # 크림슨 발록: 11003817
        destroy_monster(spawnIds=[122]) # 크림슨 참모: 11003816
        destroy_monster(spawnIds=[123]) # 크림슨 스피어1: 11003816
        destroy_monster(spawnIds=[124]) # 크림슨 스피어2: 11003816
        destroy_monster(spawnIds=[125]) # 크림슨 스피어3: 11003816
        destroy_monster(spawnIds=[126]) # 크림슨 스피어4: 11003816
        reset_camera(interpolationTime=1)
        visible_my_pc(isVisible=True) # 유저 투명 해제

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 조작_시작()


class 조작_시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        set_event_ui(type=1, arg2='$52010056_QD__EventSection__17$', arg3='3000', arg4='0')
        set_quest_accept(questId=91000053)
        set_visible_ui(uiNames=['UpperHudDialog','MessengerBrowser','ExpBar','GroupMessengerBrowser','QuestGuideDialog','MinimapDialog','AdPushDialog','SnowmanEventDialog'], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2010], questIds=[91000054], questStates=[2]):
            return 의외의효능_화면끔()
        if quest_user_detected(boxIds=[2010], questIds=[91000054], questStates=[1]):
            return 의외의효능_화면끔()

    def on_exit(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_sound(triggerId=7001, arg2=False)


#  여기서부터 각성 연출 
class 의외의효능_화면끔(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 의외의효능_준비()

    def on_exit(self):
        visible_my_pc(isVisible=False) # 유저 투명화
        create_monster(spawnIds=[102], arg2=False) # 트리스탄: 11003812
        destroy_monster(spawnIds=[111])
        destroy_monster(spawnIds=[112])
        destroy_monster(spawnIds=[121])
        destroy_monster(spawnIds=[122])
        destroy_monster(spawnIds=[123])
        destroy_monster(spawnIds=[124])
        destroy_monster(spawnIds=[125])
        destroy_monster(spawnIds=[126])


class 의외의효능_준비(state.State):
    def on_enter(self):
        remove_buff(boxId=2001, skillId=99910300)
        select_camera_path(pathIds=[4008], returnView=False)
        move_user(mapId=52010056, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 의외의효능_연출A()


class 의외의효능_연출A(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__18$', duration=4569)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4569):
            return 의외의효능_연출B()


class 의외의효능_연출B(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5005], visible=True)
        set_effect(triggerIds=[5008], visible=True)
        create_monster(spawnIds=[801], arg2=False) # 크림슨 스피어1: 11003816
        select_camera_path(pathIds=[4009,4010], returnView=False)
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__19$', duration=2800)
        set_scene_skip(state=각성_전투준비, arg2='nextState') # 트리스탄 각성 전투로 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 포털생성()


class 포털생성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5008], visible=False)
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__20$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 크림슨군단생성()


class 크림슨군단생성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5006], visible=True)
        set_effect(triggerIds=[5007], visible=True)
        set_effect(triggerIds=[5009], visible=True)
        set_effect(triggerIds=[5010], visible=True)
        set_effect(triggerIds=[5012], visible=True)
        set_effect(triggerIds=[5013], visible=True)
        create_monster(spawnIds=[802], arg2=False) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[803], arg2=False) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[804], arg2=False) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[805], arg2=False) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[806], arg2=False) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[807], arg2=False) # 크림슨 스피어1: 11003816

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 크림슨군단진영()


class 크림슨군단진영(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5006], visible=False)
        set_effect(triggerIds=[5007], visible=False)
        set_effect(triggerIds=[5009], visible=False)
        set_effect(triggerIds=[5010], visible=False)
        set_effect(triggerIds=[5012], visible=False)
        set_effect(triggerIds=[5013], visible=False)
        set_npc_emotion_sequence(spawnId=801, sequenceName='Stun_A')
        move_npc(spawnId=802, patrolName='MS2PatrolData_3009')
        move_npc(spawnId=803, patrolName='MS2PatrolData_3010')
        move_npc(spawnId=804, patrolName='MS2PatrolData_3011')
        move_npc(spawnId=805, patrolName='MS2PatrolData_3012')
        move_npc(spawnId=806, patrolName='MS2PatrolData_3013')
        move_npc(spawnId=807, patrolName='MS2PatrolData_3014')
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__21$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 크림슨발록분노()


class 크림슨발록분노(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=801, sequenceName='Attack_01_B')
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__22$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄대사_A()

    def on_exit(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬


class 트리스탄대사_A(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__23$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄대사_B()


class 트리스탄대사_B(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__24$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크림슨발록대사_A()


class 크림슨발록대사_A(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011], returnView=False)
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__25$', duration=2800, illustId='balrog_normal', align='Center')
        set_effect(triggerIds=[5011], visible=True) # 몸체 이펙트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_A()

    def on_exit(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔


class 인페르녹의혼_흡수연출_A(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=102, sequenceName='Attack_02_B', duration=1E+09)
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__26$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_B()


class 인페르녹의혼_흡수연출_B(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4012], returnView=False)
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__27$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_C()


class 인페르녹의혼_흡수연출_C(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5012], visible=True) # 몸체 이펙트
        set_effect(triggerIds=[5013], visible=True) # 펑
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__28$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 인페르녹의혼_흡수연출_D()


class 인페르녹의혼_흡수연출_D(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 인페르녹의혼_흡수연출_E()


class 인페르녹의혼_흡수연출_E(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__29$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_F()


class 인페르녹의혼_흡수연출_F(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__30$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_G()


class 인페르녹의혼_흡수연출_G(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__31$', duration=2800, align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_H()


class 인페르녹의혼_흡수연출_H(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__32$', duration=2800, align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_I()


class 인페르녹의혼_흡수연출_I(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__33$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_J()


class 인페르녹의혼_흡수연출_J(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__34$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_K()


class 인페르녹의혼_흡수연출_K(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__35$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_L()


class 인페르녹의혼_흡수연출_L(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__36$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_M()


class 인페르녹의혼_흡수연출_M(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__37$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹의혼_흡수연출_N()


class 인페르녹의혼_흡수연출_N(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013], returnView=False)
        add_cinematic_talk(npcId=11003821, msg='$52010056_QD__EventSection__38$', duration=2800)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 각성_전투준비()


class 각성_전투준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_mesh(triggerIds=[9005], visible=False)
        set_mesh_animation(triggerIds=[9005], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[9006], visible=True)
        set_mesh_animation(triggerIds=[9006], visible=True, arg3=0, arg4=0)
        destroy_monster(spawnIds=[102]) # 트리스탄
        destroy_monster(spawnIds=[802])
        destroy_monster(spawnIds=[803])
        destroy_monster(spawnIds=[804])
        destroy_monster(spawnIds=[805])
        destroy_monster(spawnIds=[806])
        destroy_monster(spawnIds=[807])
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5006], visible=False)
        set_effect(triggerIds=[5007], visible=False)
        set_effect(triggerIds=[5008], visible=False)
        set_effect(triggerIds=[5009], visible=False)
        set_effect(triggerIds=[5010], visible=False)
        set_effect(triggerIds=[5009], visible=False)
        set_effect(triggerIds=[5010], visible=False)
        set_effect(triggerIds=[5011], visible=False)
        set_effect(triggerIds=[5012], visible=False)
        set_effect(triggerIds=[5013], visible=False)
        visible_my_pc(isVisible=True) # 유저 투명 해제
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 각성_전투시작()


class 각성_전투시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__39$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 조작제어_해제()


class 조작제어_해제(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 크림슨발록군단생성_A()


class 크림슨발록군단생성_A(state.State):
    def on_enter(self):
        create_monster(spawnIds=[701], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[702], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[703], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[704], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[705], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[706], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[707], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[708], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[709], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[710], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[711], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[712], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[713], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[714], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[715], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[716], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[717], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[718], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[719], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[720], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[721], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[722], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[723], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[724], arg2=True) # 크림슨 스피어1: 11003816
        set_event_ui(type=1, arg2='$52010056_QD__EventSection__40$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크림슨발록군단생성_B()


class 크림슨발록군단생성_B(state.State):
    def on_enter(self):
        create_monster(spawnIds=[701], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[702], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[703], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[704], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[705], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[706], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[707], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[708], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[709], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[710], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[711], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[712], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[713], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[714], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[715], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[716], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[717], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[718], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[719], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[720], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[721], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[722], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[723], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[724], arg2=True) # 크림슨 스피어1: 11003816

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크림슨발록군단생성_C()


class 크림슨발록군단생성_C(state.State):
    def on_enter(self):
        create_monster(spawnIds=[701], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[702], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[703], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[704], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[705], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[706], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[707], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[708], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[709], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[710], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[711], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[712], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[713], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[714], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[715], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[716], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[717], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[718], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[719], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[720], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[721], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[722], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[723], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[724], arg2=True) # 크림슨 스피어1: 11003816

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 크림슨발록군단생성_D()


class 크림슨발록군단생성_D(state.State):
    def on_enter(self):
        create_monster(spawnIds=[701], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[702], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[703], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[704], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[705], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[706], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[707], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[708], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[709], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[710], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[711], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[712], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[713], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[714], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[715], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[716], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[717], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[718], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[719], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[720], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[721], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[722], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[723], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[724], arg2=True) # 크림슨 스피어1: 11003816
        set_event_ui(type=1, arg2='$52010056_QD__EventSection__41$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 크림슨발록군단생성_E()


class 크림슨발록군단생성_E(state.State):
    def on_enter(self):
        create_monster(spawnIds=[701], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[702], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[703], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[704], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[705], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[706], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[707], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[708], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[709], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[710], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[711], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[712], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[713], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[714], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[715], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[716], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[717], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[718], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[719], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[720], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[721], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[722], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[723], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[724], arg2=True) # 크림슨 스피어1: 11003816

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 크림슨발록군단생성_F()


class 크림슨발록군단생성_F(state.State):
    def on_enter(self):
        create_monster(spawnIds=[701], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[702], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[703], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[704], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[705], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[706], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[707], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[708], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[709], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[710], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[711], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[712], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[713], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[714], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[715], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[716], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[717], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[718], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[719], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[720], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[721], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[722], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[723], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[724], arg2=True) # 크림슨 스피어1: 11003816

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724]):
            return 필살기연출_암전()


class 필살기연출_암전(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False) # 유저 투명
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬
        move_user(mapId=52010056, portalId=6003)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 필살기연출_준비A()


class 필살기연출_준비A(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[701])
        destroy_monster(spawnIds=[702])
        destroy_monster(spawnIds=[703])
        destroy_monster(spawnIds=[704])
        destroy_monster(spawnIds=[705])
        destroy_monster(spawnIds=[706])
        destroy_monster(spawnIds=[707])
        destroy_monster(spawnIds=[708])
        destroy_monster(spawnIds=[709])
        destroy_monster(spawnIds=[710])
        destroy_monster(spawnIds=[711])
        destroy_monster(spawnIds=[712])
        destroy_monster(spawnIds=[713])
        destroy_monster(spawnIds=[714])
        destroy_monster(spawnIds=[715])
        destroy_monster(spawnIds=[716])
        destroy_monster(spawnIds=[717])
        destroy_monster(spawnIds=[718])
        destroy_monster(spawnIds=[719])
        destroy_monster(spawnIds=[720])
        destroy_monster(spawnIds=[721])
        destroy_monster(spawnIds=[722])
        destroy_monster(spawnIds=[723])
        destroy_monster(spawnIds=[724])
        create_monster(spawnIds=[103], arg2=True) # 트리스탄
        create_monster(spawnIds=[808], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[809], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[810], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[811], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[812], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[813], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[814], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[815], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[816], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[817], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[818], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[819], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[820], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[821], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[822], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[823], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[824], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[825], arg2=True) # 크림슨 스피어1: 11003816
        create_monster(spawnIds=[826], arg2=True) # 크림슨 스피어1: 11003816

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 필살기연출_준비B()


class 필살기연출_준비B(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=103, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=808, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=809, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=810, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=811, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=812, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=813, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=814, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=815, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=816, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=817, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=818, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=819, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=820, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=821, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=822, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=823, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=824, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=825, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=826, sequenceName='Attack_Idle_A', duration=9999999)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 카메라_온A()


class 카메라_온A(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        select_camera_path(pathIds=[4014], returnView=False)
        set_scene_skip(state=트리거업적, arg2='nextState') # 크림슨 발록 연출 스킵

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 카메라_온B()


class 카메라_온B(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4015], returnView=False)
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__42$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 카메라_온C()


class 카메라_온C(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4016], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 카메라_리셋()


class 카메라_리셋(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 크림슨발록_대사_G()


class 크림슨발록_대사_G(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=801, sequenceName='Attack_01_B')
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__43$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄_대사_H()


class 트리스탄_대사_H(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__44$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크림슨발록_대사_I()


class 크림슨발록_대사_I(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__45$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄_대사D()


class 트리스탄_대사D(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__46$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄_대사E()


class 트리스탄_대사E(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__47$', duration=2800, illustId='Tristan_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 필살기연출_모션A()


class 필살기연출_모션A(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=103, sequenceName='Attack_02_B', duration=9999999)
        set_effect(triggerIds=[5014], visible=True) # 트리스탄 바닥이펙트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 필살기연출_모션B()


class 필살기연출_모션B(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=103, sequenceName='Attack_01_B', duration=9999999)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 크림슨발록_대사_J()


class 크림슨발록_대사_J(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__48$', duration=1800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1800):
            return 크림슨발록_대사_K()


class 크림슨발록_대사_K(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # 트리스탄 바닥이펙트
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__55$', duration=1800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_A()


class 바닥이펙트_A(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=808, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5102], visible=True)
        set_effect(triggerIds=[5202], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_B()


class 바닥이펙트_B(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=809, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5103], visible=True)
        set_effect(triggerIds=[5203], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_C()


class 바닥이펙트_C(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=810, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5104], visible=True)
        set_effect(triggerIds=[5204], visible=True)
        set_effect(triggerIds=[5302], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_D()


class 바닥이펙트_D(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=811, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5105], visible=True)
        set_effect(triggerIds=[5205], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_E()


class 바닥이펙트_E(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=812, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5106], visible=True)
        set_effect(triggerIds=[5206], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_F()


class 바닥이펙트_F(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=813, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5107], visible=True)
        set_effect(triggerIds=[5207], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_G()


class 바닥이펙트_G(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=814, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5108], visible=True)
        set_effect(triggerIds=[5208], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_H()


class 바닥이펙트_H(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=815, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5109], visible=True)
        set_effect(triggerIds=[5209], visible=True)
        set_effect(triggerIds=[5303], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_I()


class 바닥이펙트_I(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=816, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5110], visible=True)
        set_effect(triggerIds=[5210], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_J()


class 바닥이펙트_J(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=817, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5111], visible=True)
        set_effect(triggerIds=[5211], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_K()


class 바닥이펙트_K(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=818, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5112], visible=True)
        set_effect(triggerIds=[5212], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_L()


class 바닥이펙트_L(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=819, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5113], visible=True)
        set_effect(triggerIds=[5213], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_M()


class 바닥이펙트_M(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=820, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5114], visible=True)
        set_effect(triggerIds=[5214], visible=True)
        set_effect(triggerIds=[5304], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_N()


class 바닥이펙트_N(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=821, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5115], visible=True)
        set_effect(triggerIds=[5215], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_O()


class 바닥이펙트_O(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=822, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5116], visible=True)
        set_effect(triggerIds=[5216], visible=True)
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml') # 페이드 아웃 켬

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_P()


class 바닥이펙트_P(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=823, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5117], visible=True)
        set_effect(triggerIds=[5217], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_Q()


class 바닥이펙트_Q(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=824, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5118], visible=True)
        set_effect(triggerIds=[5218], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 바닥이펙트_R()


class 바닥이펙트_R(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=825, sequenceName='Damg_A', duration=9999999)
        set_effect(triggerIds=[5202], visible=True)
        set_effect(triggerIds=[5301], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크림슨발록_대사_L()


class 크림슨발록_대사_L(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003817, msg='$52010056_QD__EventSection__50$', duration=2800, illustId='balrog_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마지막연출_세팅()

    def on_exit(self):
        destroy_monster(spawnIds=[103])
        create_monster(spawnIds=[104], arg2=True) # 트리스탄


class 마지막연출_세팅(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=False)
        set_effect(triggerIds=[5102], visible=False)
        set_effect(triggerIds=[5103], visible=False)
        set_effect(triggerIds=[5104], visible=False)
        set_effect(triggerIds=[5105], visible=False)
        set_effect(triggerIds=[5106], visible=False)
        set_effect(triggerIds=[5107], visible=False)
        set_effect(triggerIds=[5108], visible=False)
        set_effect(triggerIds=[5109], visible=False)
        set_effect(triggerIds=[5110], visible=False)
        set_effect(triggerIds=[5111], visible=False)
        set_effect(triggerIds=[5112], visible=False)
        set_effect(triggerIds=[5113], visible=False)
        set_effect(triggerIds=[5114], visible=False)
        set_effect(triggerIds=[5115], visible=False)
        set_effect(triggerIds=[5116], visible=False)
        set_effect(triggerIds=[5117], visible=False)
        set_effect(triggerIds=[5118], visible=False)
        set_effect(triggerIds=[5201], visible=False)
        set_effect(triggerIds=[5202], visible=False)
        set_effect(triggerIds=[5203], visible=False)
        set_effect(triggerIds=[5204], visible=False)
        set_effect(triggerIds=[5205], visible=False)
        set_effect(triggerIds=[5206], visible=False)
        set_effect(triggerIds=[5207], visible=False)
        set_effect(triggerIds=[5208], visible=False)
        set_effect(triggerIds=[5209], visible=False)
        set_effect(triggerIds=[5210], visible=False)
        set_effect(triggerIds=[5211], visible=False)
        set_effect(triggerIds=[5212], visible=False)
        set_effect(triggerIds=[5213], visible=False)
        set_effect(triggerIds=[5214], visible=False)
        set_effect(triggerIds=[5215], visible=False)
        set_effect(triggerIds=[5216], visible=False)
        set_effect(triggerIds=[5218], visible=False)
        set_effect(triggerIds=[5218], visible=False)
        set_effect(triggerIds=[5301], visible=False)
        set_effect(triggerIds=[5302], visible=False)
        set_effect(triggerIds=[5303], visible=False)
        set_effect(triggerIds=[5304], visible=False)
        reset_camera(interpolationTime=0)
        set_npc_emotion_loop(spawnId=104, sequenceName='Attack_Idle_A', duration=9999999)
        set_npc_emotion_loop(spawnId=801, sequenceName='Dead_01_A', duration=9999999)
        set_npc_emotion_loop(spawnId=808, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=809, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=810, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=811, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=812, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=813, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=814, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=815, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=816, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=817, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=818, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=819, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=820, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=821, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=822, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=823, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=824, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=825, sequenceName='Dead_A', duration=9999999)
        set_npc_emotion_loop(spawnId=826, sequenceName='Dead_A', duration=9999999)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마지막연출_온()


class 마지막연출_온(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml') # 페이드 아웃 켬

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리스탄_대사F()


class 트리스탄_대사F(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003812, msg='$52010056_QD__EventSection__51$', duration=2800, illustId='Tristan_normal', align='Center')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리거업적()


class 트리거업적(state.State):
    def on_enter(self):
        set_achievement(triggerId=2009, type='trigger', achieve='tristanarousal')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        move_user(mapId=52010052, portalId=1)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[2]):
            return 연출종료()


