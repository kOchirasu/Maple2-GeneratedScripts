""" trigger/52010027_qd/main.xml """
from common import *
import state


#  바람의 골짜기 : 52010027  
class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003073], questStates=[1]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301], arg2=True) # 습격지역 꼭대기 집
        create_monster(spawnIds=[302], arg2=True) # 습격지역 꼭대기 입구
        create_monster(spawnIds=[303], arg2=True) # 습격지역 꼭대기 주민
        create_monster(spawnIds=[304], arg2=True) # 진입부 주민 1층
        create_monster(spawnIds=[305], arg2=True) # 진입부 주민 2층
        create_monster(spawnIds=[401], arg2=True) # 악당NPC_1
        create_monster(spawnIds=[402], arg2=True) # 악당NPC_2
        create_monster(spawnIds=[403], arg2=True) # 악당NPC_3
        create_monster(spawnIds=[404], arg2=True) # 악당NPC_4
        create_monster(spawnIds=[405], arg2=True) # 악당NPC_5
        create_monster(spawnIds=[406], arg2=True) # 악당NPC_6
        create_monster(spawnIds=[407], arg2=True) # 악당NPC_7
        create_monster(spawnIds=[408], arg2=True) # 악당NPC_8
        create_monster(spawnIds=[409], arg2=True) # 악당NPC_9
        create_monster(spawnIds=[501], arg2=True) # 보스NPC_1
        create_monster(spawnIds=[502], arg2=True) # 보스NPC_1
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라_전환()


class 카메라_전환(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        show_caption(type='VerticalCaption', title='$52010027_QD__MAIN__0$', desc='$52010027_QD__MAIN__1$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        set_npc_emotion_loop(spawnId=303, sequenceName='Down_Idle_A', duration=150000)
        face_emotion(spawnId=302, emotionName='down_Idle')
        face_emotion(spawnId=303, emotionName='down_Idle')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 연출_습격현장()


class 연출_습격현장(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        add_balloon_talk(spawnId=301, msg='$52010027_QD__MAIN__2$', duration=3000, delayTick=0)
        add_balloon_talk(spawnId=403, msg='$52010027_QD__MAIN__3$', duration=3000, delayTick=0)
        add_balloon_talk(spawnId=303, msg='$52010027_QD__MAIN__4$', duration=2000, delayTick=1000)
        set_npc_emotion_sequence(spawnId=402, sequenceName='Attack_02_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4200):
            return 연출_습격현장_02()


class 연출_습격현장_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출_습격현장_02_01()


class 연출_습격현장_02_01(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=401, msg='$52010027_QD__MAIN__5$', duration=2000, delayTick=0)
        set_npc_emotion_sequence(spawnId=401, sequenceName='Attack_02_A')
        add_balloon_talk(spawnId=304, msg='$52010027_QD__MAIN__6$', duration=2000, delayTick=500)
        add_balloon_talk(spawnId=305, msg='$52010027_QD__MAIN__7$', duration=3000, delayTick=1500)
        set_npc_emotion_loop(spawnId=305, sequenceName='Down_Idle_A', duration=150000)
        face_emotion(spawnId=304, emotionName='down_Idle')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 연출_습격현장확인_PC()


class 연출_습격현장확인_PC(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__8$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__9$', duration=3000)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=10000)
        add_balloon_talk(spawnId=0, msg='$52010027_QD__MAIN__10$', duration=2000, delayTick=6000)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__11$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 연출_습격현장_보스등장()


class 연출_습격현장_보스등장(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4010], returnView=False)
        move_npc(spawnId=502, patrolName='MS2PatrolData_3004')
        show_caption(type='VerticalCaption', title='$52010027_QD__MAIN__12$', desc='$52010027_QD__MAIN__13$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__14$', duration=3500)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__15$', duration=3500)
        add_balloon_talk(spawnId=405, msg='$52010027_QD__MAIN__16$', duration=2000, delayTick=2000)
        add_balloon_talk(spawnId=406, msg='$52010027_QD__MAIN__17$', duration=2000, delayTick=1800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출_습격현장_보스이동()


class 연출_습격현장_보스이동(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=501, sequenceName='Attack_01_G')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출_습격현장_보스소환연출()


class 연출_습격현장_보스소환연출(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[502]) # 보스NPC_1
        set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출_습격현장_보스소환연출_02()


class 연출_습격현장_보스소환연출_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 연출_습격현장_보스소환연출_03()


class 연출_습격현장_보스소환연출_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__18$', duration=3000)
        set_npc_emotion_sequence(spawnId=501, sequenceName='Attack_01_D')
        move_user(mapId=52010027, portalId=6001)
        destroy_monster(spawnIds=[401])
        destroy_monster(spawnIds=[402])
        destroy_monster(spawnIds=[403])
        destroy_monster(spawnIds=[404])
        destroy_monster(spawnIds=[405])
        destroy_monster(spawnIds=[406])
        destroy_monster(spawnIds=[407])
        destroy_monster(spawnIds=[408])
        destroy_monster(spawnIds=[409])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3800):
            return 연출_습격현장_PC연출()


class 연출_습격현장_PC연출(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=3500)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__19$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출_습격현장_PC연출_1()


class 연출_습격현장_PC연출_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출_습격현장_전투준비()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        move_user(mapId=52010027, portalId=6001)
        set_effect(triggerIds=[5002], visible=True)
        destroy_monster(spawnIds=[502]) # 보스NPC_1
        destroy_monster(spawnIds=[401])
        destroy_monster(spawnIds=[402])
        destroy_monster(spawnIds=[403])
        destroy_monster(spawnIds=[404])
        destroy_monster(spawnIds=[405])
        destroy_monster(spawnIds=[406])
        destroy_monster(spawnIds=[407])
        destroy_monster(spawnIds=[408])
        destroy_monster(spawnIds=[409])
        select_camera_path(pathIds=[4008], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출_습격현장_전투준비()


class 연출_습격현장_전투준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[601], arg2=True) # 악당Mob_1
        create_monster(spawnIds=[602], arg2=True) # 악당Mob_2
        create_monster(spawnIds=[603], arg2=True) # 악당Mob_3
        create_monster(spawnIds=[604], arg2=True) # 악당Mob_4
        create_monster(spawnIds=[605], arg2=True) # 악당Mob_5
        create_monster(spawnIds=[606], arg2=True) # 악당Mob_6
        add_balloon_talk(spawnId=602, msg='$52010027_QD__MAIN__20$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=606, msg='$52010027_QD__MAIN__21$', duration=2000, delayTick=500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출_습격현장_전투준비_02()


class 연출_습격현장_전투준비_02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차_전투1()


class 차_전투1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52010027_QD__MAIN__22$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,602,603,604,605,606]):
            return 연출_잠시쉬기()


class 연출_잠시쉬기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차_전투_보스몬스터대사1()


class 차_전투_보스몬스터대사1(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_2, arg2='nextState')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__23$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차_전투_보스소환연출2()


class 차_전투_보스소환연출2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__24$', duration=3000)
        set_npc_emotion_sequence(spawnId=501, sequenceName='Attack_01_C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차_전투_보스소환연출_1_2()


class 차_전투_보스소환연출_1_2(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차_전투2()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차_전투2()


class 차_전투2(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_event_ui(type=1, arg2='$52010027_QD__MAIN__25$', arg3='3000', arg4='0')
        create_monster(spawnIds=[701], arg2=True) # 악당Mob_1
        create_monster(spawnIds=[702], arg2=True) # 악당Mob_2
        create_monster(spawnIds=[703], arg2=True) # 악당Mob_3
        create_monster(spawnIds=[704], arg2=True) # 악당Mob_4
        create_monster(spawnIds=[705], arg2=True) # 악당Mob_5
        create_monster(spawnIds=[706], arg2=True) # 악당Mob_6
        add_balloon_talk(spawnId=701, msg='$52010027_QD__MAIN__26$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=703, msg='$52010027_QD__MAIN__27$', duration=2000, delayTick=500)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[701,702,703,704,705,706]):
            return 연출_잠시쉬기_01()


class 연출_잠시쉬기_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출_페리온영웅등장()


class 연출_페리온영웅등장(state.State):
    def on_enter(self):
        set_achievement(triggerId=2001, type='trigger', achieve='Windvalley')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_loop(spawnId=501, sequenceName='Attack_Idle_A', duration=16000)
        set_scene_skip(state=페리온으로, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출_페리온영웅등장_보스대사()


class 연출_페리온영웅등장_보스대사(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__28$', duration=3000)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__29$', duration=3000)
        destroy_monster(spawnIds=[601])
        destroy_monster(spawnIds=[602])
        destroy_monster(spawnIds=[603])
        destroy_monster(spawnIds=[604])
        destroy_monster(spawnIds=[605])
        destroy_monster(spawnIds=[606])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 연출_페리온영웅등장_보스대사_02()


class 연출_페리온영웅등장_보스대사_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004,4015], returnView=False)
        add_balloon_talk(spawnId=501, msg='$52010027_QD__MAIN__30$', duration=2000, delayTick=0)
        add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__31$', duration=3000)
        add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__32$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 연출_페리온영웅등장_보스대사_03()


class 연출_페리온영웅등장_보스대사_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        add_balloon_talk(spawnId=501, msg='$52010027_QD__MAIN__33$', duration=2000, delayTick=0)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__34$', duration=3000)
        create_monster(spawnIds=[201], arg2=True) # 에바고르: 11003391
        create_monster(spawnIds=[101], arg2=True) # 시끄러운 주먹: 11003388

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 연출_페리온영웅등장_02()


class 연출_페리온영웅등장_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        select_camera_path(pathIds=[4015,4006], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        show_caption(type='VerticalCaption', title='$52010027_QD__MAIN__35$', desc='$52010027_QD__MAIN__36$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__37$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출_페리온영웅등장_03()


class 연출_페리온영웅등장_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__38$', duration=3000)
        add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__39$', duration=3000)
        move_npc(spawnId=101, patrolName='MS2PatrolData_3002')
        move_npc(spawnId=201, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 연출_페리온영웅등장_04()


class 연출_페리온영웅등장_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__40$', duration=3000)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN__41$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출_페리온영웅등장_05()


class 연출_페리온영웅등장_05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        destroy_monster(spawnIds=[501])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출_페리온영웅과대화()


class 연출_페리온영웅과대화(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_npc_emotion_loop(spawnId=101, sequenceName='Bore_B', duration=3000)
        set_npc_emotion_loop(spawnId=201, sequenceName='Attack_Idle_A', duration=3000)
        add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__42$', duration=3500)
        add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__43$', duration=2000)
        add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__44$', duration=3500)
        move_user(mapId=52010027, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 연출_페리온영웅과대화_02()


class 연출_페리온영웅과대화_02(state.State):
    def on_enter(self):
        face_emotion(spawnId=201, emotionName='Trigger_NotAgree')
        select_camera_path(pathIds=[4010], returnView=False)
        set_pc_emotion_loop(sequenceName='Talk_A', duration=29000)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__45$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출_페리온영웅과대화_03()


class 연출_페리온영웅과대화_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        face_emotion(spawnId=201, emotionName='Trigger_NotAgree')
        add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__46$', duration=3000)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__47$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 연출_페리온영웅과대화_04()


class 연출_페리온영웅과대화_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010], returnView=False)
        set_pc_emotion_loop(sequenceName='Talk_A', duration=29000)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__48$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN__49$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출_페리온영웅과대화_05()


class 연출_페리온영웅과대화_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=15000)
        face_emotion(spawnId=201, emotionName='Trigger_Sad')
        add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__50$', duration=3000)
        add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__51$', duration=3000)
        add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__52$', duration=2000)
        add_cinematic_talk(npcId=11003391, msg='$52010027_QD__MAIN__53$', duration=2000)
        add_cinematic_talk(npcId=11003388, msg='$52010027_QD__MAIN__54$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return 연출_페리온영웅과대화_05_1()


class 연출_페리온영웅과대화_05_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 페리온으로()


class 페리온으로(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_portal(portalId=6003, visible=True, enabled=True, minimapVisible=True)
        move_user(mapId=52010027, portalId=6004)
        destroy_monster(spawnIds=[201]) # 에바고르: 11003391
        destroy_monster(spawnIds=[101]) # 시끄러운 주먹: 11003388

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 페리온으로02()


class 페리온으로02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 페리온으로03()


class 페리온으로03(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52010027_QD__MAIN__55$', arg3='3000', arg4='0')


