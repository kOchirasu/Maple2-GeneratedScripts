""" trigger/52010027_qd/main_quest10003101.xml """
from common import *
import state


#  바람의 골짜기 : 52010027  
#  중간 보스 빌런과 전투 벌이는 씬  
class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5005], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003101], questStates=[1]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52010027, portalId=6005)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 집에서나옴()


class 집에서나옴(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3006')
        create_monster(spawnIds=[801], arg2=True)
        add_balloon_talk(spawnId=0, msg='$52010027_QD__MAIN_QUEST10003101__0$', duration=3000, delayTick=500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 집에서나와서대사침()


class 집에서나와서대사침(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Suprise_A'])
        add_balloon_talk(spawnId=0, msg='$52010027_QD__MAIN_QUEST10003101__1$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 집에나와서대사침01()


class 집에나와서대사침01(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=10000)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003101__2$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 집에나와서대사침02()


class 집에나와서대사침02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4012], returnView=False)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__3$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 집에나와서대사침03()


class 집에나와서대사침03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011], returnView=False)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=10000)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003101__4$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 집에나와서대사침04()


class 집에나와서대사침04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4012], returnView=False)
        move_npc(spawnId=801, patrolName='MS2PatrolData_3005')
        set_effect(triggerIds=[5005], visible=True)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__5$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003101__6$', duration=3000)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__7$', duration=3000)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__8$', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003101__9$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return 집에나와서대사침05()


class 집에나와서대사침05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=801, sequenceName='Attack_01_G')
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__10$', duration=3000)
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__11$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 전투시작01()


class 전투시작01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52010027, portalId=6006)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투시작01_1()


class 전투시작01_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투시작02()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        move_user(mapId=52010027, portalId=6006)
        create_monster(spawnIds=[801], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투시작02()


class 전투시작02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5005], visible=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[801])
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투시작03()


class 전투시작03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[802], arg2=True)
        set_event_ui(type=1, arg2='$52010027_QD__MAIN_QUEST10003101__12$', arg3='3000', arg4='0')
        add_balloon_talk(spawnId=802, msg='$52010027_QD__MAIN_QUEST10003101__13$', duration=3000, delayTick=5000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[802]):
            return 전투종료01()


class 전투종료01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52010027, portalId=6007)
        destroy_monster(spawnIds=[802])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전투종료02()


class 전투종료02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__14$', duration=3000)
        set_npc_emotion_loop(spawnId=803, sequenceName='Stun_A', duration=160000000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투종료03()


class 전투종료03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None # Missing State: 


