""" trigger/52000112_qd/52000112.xml """
from common import *
import state


class START(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5300], visible=False) # 재즈바 비밀통로 경로 안내
        create_monster(spawnIds=[101], arg2=False) # 바텐더
        set_actor(triggerId=231, visible=True, initialSequence='Closed')
        set_effect(triggerIds=[400], visible=False)
        set_effect(triggerIds=[401], visible=False)
        set_effect(triggerIds=[402], visible=False)
        set_effect(triggerIds=[403], visible=False)
        set_effect(triggerIds=[404], visible=False)
        set_effect(triggerIds=[405], visible=False)
        set_effect(triggerIds=[406], visible=False)
        set_effect(triggerIds=[407], visible=False)
        set_mesh(triggerIds=[300,301,302,303,304,305,306,307], visible=True, arg3=0, arg4=1000, arg5=1000) # 큐브하나씩부셔지는연출

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002306], questStates=[2]):
            return 재즈바1층습격_완료가능01()
        if quest_user_detected(boxIds=[10011], questIds=[20002306], questStates=[1]):
            return 재즈바1층습격_진행중01()
        if quest_user_detected(boxIds=[10011], questIds=[20002308], questStates=[2]):
            return 재즈바_지하습격_완료가능01()
        if quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[2]):
            return 쉐도우클로전투_완료연출01()
        if quest_user_detected(boxIds=[10011], questIds=[20002311], questStates=[3]):
            return 재즈바_지하습격_완료가능01()
        if quest_user_detected(boxIds=[10011], questIds=[20002308], questStates=[3]):
            return 재즈바_지하습격_완료가능01()
        if quest_user_detected(boxIds=[10011], questIds=[20002306], questStates=[3]):
            return 재즈바1층습격_완료가능01()


#  ########################씬1 재즈바_1층습격########################
class 재즈바1층습격_진행중01(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[102,103,104,105,106,107], isAutoTargeting=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002306], questStates=[2]):
            return 재즈바1층습격_완료가능01_b()


class 재즈바1층습격_완료가능01_b(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='$52000112_QD__52000112__0$', duration=6000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 재즈바1층습격_완료가능01()


class 재즈바1층습격_완료가능01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 재즈바1층습격_완료가능02()


class 재즈바1층습격_완료가능02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[200], arg2=False)
        destroy_monster(spawnIds=[102,103,104,105,106,107])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 재즈바1층습격_완료가능03()


class 재즈바1층습격_완료가능03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        create_monster(spawnIds=[111], arg2=False)
        move_npc(spawnId=111, patrolName='MS2PatrolData_shadowClawMove') # 쉐도우클로 이동
        add_balloon_talk(spawnId=111, msg='$52000112_QD__52000112__1$', duration=6000, delayTick=1000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002308], questStates=[1]):
            return 재즈바_지하습격_진행중01()


#  ########################씬2 재즈바_지하습격########################
class 재즈바_지하습격_진행중01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5300], visible=True) # 재즈바 비밀통로 경로 안내
        set_actor(triggerId=231, visible=True, initialSequence='Opened')
        create_monster(spawnIds=[200,209,204,205,210,206], arg2=False) # 지하층 다크윈드 요원 생성

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002308], questStates=[2]):
            return 재즈바_지하습격_완료가능01_b()


class 재즈바_지하습격_완료가능01_b(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='$52000112_QD__52000112__2$', duration=6000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 재즈바_지하습격_완료가능01()


class 재즈바_지하습격_완료가능01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 재즈바_지하습격_완료가능02()


class 재즈바_지하습격_완료가능02(state.State):
    def on_enter(self):
        set_onetime_effect(id=20, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        create_monster(spawnIds=[208], arg2=False) # 쉐도우클로
        create_monster(spawnIds=[201,202,203], arg2=False) # 다크윈드 포로
        create_monster(spawnIds=[211,212,213,214,215,216,217,218,219], arg2=False) # 로그스 대원
        destroy_monster(spawnIds=[108,109,110,111,200,209,204,205,210,206])
        move_user(mapId=52000112, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 재즈바_지하습격_완료가능03()


class 재즈바_지하습격_완료가능03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002311], questStates=[3]):
            return PC_로그스거역_진행중01()


#  ########################씬3 PC_로그스거역_대원들 전투준비########################
class PC_로그스거역_진행중01(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=211, sequenceName='Attack_Idle_A', duration=15000)
        set_npc_emotion_loop(spawnId=212, sequenceName='Attack_Idle_A', duration=15000)
        set_npc_emotion_loop(spawnId=213, sequenceName='Attack_Idle_A', duration=15000)
        set_npc_emotion_loop(spawnId=214, sequenceName='Attack_Idle_A', duration=15000)
        set_npc_emotion_loop(spawnId=215, sequenceName='Attack_Idle_A', duration=15000)
        set_npc_emotion_loop(spawnId=216, sequenceName='Attack_Idle_A', duration=15000)
        set_npc_emotion_loop(spawnId=217, sequenceName='Attack_Idle_A', duration=15000)
        set_npc_emotion_loop(spawnId=218, sequenceName='Attack_Idle_A', duration=15000)
        set_npc_emotion_loop(spawnId=219, sequenceName='Attack_Idle_A', duration=15000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002312], questStates=[3]):
            return PC_로그스거역_대원들01()
        if quest_user_detected(boxIds=[10011], questIds=[20002312], questStates=[2]):
            return PC_로그스거역_대원들01()
        if quest_user_detected(boxIds=[10011], questIds=[20002312], questStates=[1]):
            return PC_로그스거역_대원들01()


#  ########################씬3 PC_로그스거역_대원들 전투########################
class PC_로그스거역_대원들01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[211,212,213,214,215,216,217,218,219]) # 로그스 대원 npc버전 삭제
        create_monster(spawnIds=[220,221,222,223,224,225,226,227,228], arg2=False) # 로그스 대원 몬스터 생성

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[1]):
            return 쉐도우클로전투_진행중01()


#  ########################씬4 쉐도우클로전투########################
class 쉐도우클로전투_진행중01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[211,212,213,214,215,216,217,218,219]) # 로그스 대원 npc버전 삭제
        destroy_monster(spawnIds=[220,221,222,223,224,225,226,227,228]) # 로그스 대원 몬스터 삭제
        set_sound(triggerId=9000, arg2=True)
        destroy_monster(spawnIds=[208])
        create_monster(spawnIds=[229], arg2=False) # 쉐도우클로

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[2]):
            return 쉐도우클로전투_완료연출01()


#  ########################씬5 쉐도우클로전투_완료연출########################
class 쉐도우클로전투_완료연출01(state.State):
    def on_enter(self):
        set_sound(triggerId=9000, arg2=False)
        visible_my_pc(isVisible=True) # 유저 투명 처리
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[207])
        create_monster(spawnIds=[208], arg2=False) # 쉐도우클로
        move_user(mapId=52000112, portalId=3)
        set_npc_emotion_loop(spawnId=208, sequenceName='Attack_Idle_A', duration=17500)
        set_npc_emotion_loop(spawnId=201, sequenceName='Sit_Down_A', duration=17500)
        set_npc_emotion_loop(spawnId=202, sequenceName='Sit_Down_A', duration=17500)
        set_npc_emotion_loop(spawnId=203, sequenceName='Sit_Down_A', duration=17500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 쉐도우클로전투_완료연출02()


class 쉐도우클로전투_완료연출02(state.State):
    def on_enter(self):
        set_scene_skip(state=쉐도우클로전투_완료연출09, arg2='exit')
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        select_camera_path(pathIds=[3000,3001], returnView=False)
        set_pc_emotion_loop(sequenceName='Push_A', duration=5000)
        face_emotion(spawnId=0, emotionName='PC_Pain_86000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 쉐도우클로전투_완료연출03()


class 쉐도우클로전투_완료연출03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3002,3003], returnView=False)
        add_cinematic_talk(npcId=11003185, illustId='0', msg='$52000112_QD__52000112__3$', duration=5000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 쉐도우클로전투_완료연출04()


class 쉐도우클로전투_완료연출04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000112_QD__52000112__4$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 쉐도우클로전투_완료연출05()


class 쉐도우클로전투_완료연출05(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=1, endScale=0.1, duration=5.5, interpolator=2) # 2초간 느려지기 시작
        select_camera_path(pathIds=[3004], returnView=False)
        set_pc_emotion_sequence(sequenceNames=['Assassin_DarkSight_A'])
        set_pc_emotion_loop(sequenceName='Assassin_DarkSight_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 쉐도우클로전투_완료연출06()


class 쉐도우클로전투_완료연출06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3005,3006], returnView=False)
        set_pc_emotion_sequence(sequenceNames=['Assassin_Enterance_A'])
        set_pc_emotion_loop(sequenceName='Assassin_Enterance_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 쉐도우클로전투_완료연출07_b()


class 쉐도우클로전투_완료연출07_b(state.State):
    def on_enter(self):
        set_effect(triggerIds=[400], visible=True)
        set_effect(triggerIds=[401], visible=True)
        set_effect(triggerIds=[402], visible=True)
        set_effect(triggerIds=[403], visible=True)
        set_effect(triggerIds=[404], visible=True)
        set_effect(triggerIds=[405], visible=True)
        set_effect(triggerIds=[406], visible=True)
        set_effect(triggerIds=[407], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1700):
            return 쉐도우클로전투_완료연출07()


class 쉐도우클로전투_완료연출07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3007,3008], returnView=False)
        add_cinematic_talk(npcId=11003185, illustId='0', msg='$52000112_QD__52000112__5$', duration=4000, align='right')
        set_npc_emotion_loop(spawnId=208, sequenceName='Stun_A', duration=15500)
        set_mesh(triggerIds=[300,301,302,303,304,305,306,307], visible=False, arg3=0, arg4=700, arg5=0) # 큐브하나씩부셔지는연출

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 쉐도우클로전투_완료연출08()


class 쉐도우클로전투_완료연출08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3009,3010], returnView=False)
        destroy_monster(spawnIds=[201,202,203])
        visible_my_pc(isVisible=False) # 유저 투명 처리
        add_cinematic_talk(npcId=11003185, illustId='0', msg='$52000112_QD__52000112__6$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 쉐도우클로전투_완료연출08_1()


class 쉐도우클로전투_완료연출08_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 쉐도우클로전투_완료연출09()


class 쉐도우클로전투_완료연출09(state.State):
    def on_enter(self):
        move_user(mapId=52000111, portalId=11)


