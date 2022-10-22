""" trigger/52000020_qd/main_02.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[60100095], questStates=[1]):
            return ready()


#  준비 
class ready(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[201])
        create_monster(spawnIds=[202], arg2=True) # 연출용 리퍼트 (11003193)
        create_monster(spawnIds=[302], arg2=True) # 연출용 흑성회 행동대장
        create_monster(spawnIds=[404,405,406,407,408,409,410,411], arg2=True) # 연출용 흑성회
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_scene_skip(state=battle_ready, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return camera()


class camera(state.State):
    def on_enter(self):
        select_camera(triggerId=4001, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start()


class start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_01()


#  이벤트 씬 시작 
class scene_01(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=False)
        set_sound(triggerId=7002, arg2=True)
        add_cinematic_talk(npcId=11003193, msg='$52000020_QD__MAIN_02__0$', duration=2000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003,4004], returnView=False)
        move_user(mapId=52000020, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=302, sequenceName='Talk_A')
        add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_02__1$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=302, sequenceName='Emotion_Angry_A')
        add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_02__2$', duration=2000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=302, sequenceName='ChatUp_A')
        add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_02__3$', duration=2000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006], returnView=False)
        set_npc_emotion_sequence(spawnId=404, sequenceName='ChatUp_A')
        set_npc_emotion_sequence(spawnId=405, sequenceName='ChatUp_A')
        set_npc_emotion_sequence(spawnId=406, sequenceName='ChatUp_A')
        set_npc_emotion_sequence(spawnId=407, sequenceName='ChatUp_A')
        set_npc_emotion_sequence(spawnId=408, sequenceName='ChatUp_A')
        set_npc_emotion_sequence(spawnId=409, sequenceName='ChatUp_A')
        set_npc_emotion_sequence(spawnId=410, sequenceName='ChatUp_A')
        set_npc_emotion_sequence(spawnId=411, sequenceName='ChatUp_A')
        add_balloon_talk(spawnId=404, msg='$52000020_QD__MAIN_02__4$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=405, msg='$52000020_QD__MAIN_02__5$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=406, msg='$52000020_QD__MAIN_02__6$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=407, msg='$52000020_QD__MAIN_02__7$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=408, msg='$52000020_QD__MAIN_02__8$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=409, msg='$52000020_QD__MAIN_02__9$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=410, msg='$52000020_QD__MAIN_02__10$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=411, msg='$52000020_QD__MAIN_02__11$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=502, sequenceName='Bore_A')
        add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_02__12$', duration=2000, align='center')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return battle_ready()


#  Round_1 전투 씬 
class battle_ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[404,405]) # 연출용 흑성회
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return battle()


class battle(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        create_monster(spawnIds=[604,605], arg2=True) # 몬스터 흑성회

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return battleMsg()


class battleMsg(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52000020_QD__MAIN_02__13$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[604,605]):
            return delay()


class delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return round_2()


class round_2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[406,407,408,409]) # 연출용 흑성회
        create_monster(spawnIds=[606,607,608,609], arg2=True) # 몬스터 흑성회

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[604,605]):
            return delay_a()


class delay_a(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return round_3()


class round_3(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[410,411,302]) # 연출용 흑성회
        create_monster(spawnIds=[610,611,502], arg2=True) # 몬스터 흑성회

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[610,611,502]):
            return delay_b()


class delay_b(state.State):
    def on_enter(self):
        set_achievement(triggerId=2002, type='trigger', achieve='mafiabattle')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return winready()


class winready(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202]) # 연출용 리퍼트
        create_monster(spawnIds=[201], arg2=True) # 퀘스트용 리퍼트(11001262)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_sound(triggerId=7002, arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return end()


class end(state.State):
    pass


