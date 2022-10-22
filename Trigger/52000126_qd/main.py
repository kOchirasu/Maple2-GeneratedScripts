""" trigger/52000126_qd/main.xml """
from common import *
import state


#  이름 없는 부랑자 (11000213) 퀘스트 / 이름 없는 부랑자(11003209) 연출  
class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True) # 이름 없는 부랑자 퀘스트 (11000213)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100210], questStates=[1]):
            return ready()


#  준비 
class ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        select_camera_path(pathIds=[4001], returnView=False)
        destroy_monster(spawnIds=[101]) # 이름 없는 부랑자 퀘스트
        create_monster(spawnIds=[102], arg2=True) # 이름 없는 부랑자 연출
        move_user(mapId=52000126, portalId=6002)
        set_scene_skip(state=battle_ready, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return talk_01()


#  이름 없는 부랑자 대사 
class talk_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_sequence(spawnId=202, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003209, msg='$52000126_QD__MAIN__0$', duration=2000, align='Left')
        create_monster(spawnIds=[301], arg2=True) # 11003214
        create_monster(spawnIds=[302], arg2=True) # 11003213
        create_monster(spawnIds=[303], arg2=True) # 11003212

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_02()


class talk_02(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=True)
        set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003209, msg='$52000126_QD__MAIN__1$', duration=2000, align='Left')
        move_npc(spawnId=301, patrolName='MS2PatrolData_3002')
        move_npc(spawnId=302, patrolName='MS2PatrolData_3003')
        move_npc(spawnId=303, patrolName='MS2PatrolData_3004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_01()


#  마스크단 등장씬 
class scene_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4003], returnView=False)
        add_cinematic_talk(npcId=11003214, msg='$52000126_QD__MAIN__2$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_sequence(spawnId=301, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003214, msg='$52000126_QD__MAIN__3$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=11003214, msg='$52000126_QD__MAIN__4$', duration=4000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005,4006,4007], returnView=False)
        add_cinematic_talk(npcId=11003214, msg='$52000126_QD__MAIN__5$', duration=3000, align='Left')
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)
        set_effect(triggerIds=[5003], visible=True)
        set_effect(triggerIds=[5004], visible=True)
        set_onetime_effect(id=20, enable=True, path='BG/Common/Sound/Eff_Object_Explosion_Debris_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3005')
        set_npc_emotion_loop(spawnId=302, sequenceName='Attack_Idle_A', duration=7000)
        set_npc_emotion_loop(spawnId=303, sequenceName='Attack_Idle_A', duration=7000)
        add_cinematic_talk(npcId=11003213, msg='$52000126_QD__MAIN__6$', duration=2000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_npc_emotion_sequence(spawnId=301, sequenceName='Attack_01_A')
        add_cinematic_talk(npcId=11003214, msg='$52000126_QD__MAIN__7$', duration=3000, align='Left')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return battle_ready()


#  전투 씬 
class battle_ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return battle()


class battle(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[301,302,303]) # 디쓰리 엔피씨
        create_monster(spawnIds=[601,602,603], arg2=True) # 디쓰리 몬스터

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return battleMsg()


class battleMsg(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52000126_QD__MAIN__8$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,602,603]):
            return end()


class end(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)
        set_achievement(triggerId=2001, type='trigger', achieve='maskbattle')
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)


