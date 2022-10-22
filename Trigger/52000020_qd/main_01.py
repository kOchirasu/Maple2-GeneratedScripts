""" trigger/52000020_qd/main_01.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True) # 퀘스트용 리퍼트(11001262)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100090], questStates=[2]):
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
        create_monster(spawnIds=[301], arg2=True)
        create_monster(spawnIds=[401,402,403], arg2=True) # 연출용 흑성회
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
        select_camera_path(pathIds=[4001,4002], returnView=False)
        set_npc_emotion_sequence(spawnId=301, sequenceName='Bore_C')
        add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_01__0$', duration=3709, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003193, msg='$52000020_QD__MAIN_01__1$', duration=3369, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003193, msg='$52000020_QD__MAIN_01__2$', duration=2000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Emotion_Troubled_A')
        add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_01__3$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Bore_B')
        add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_01__4$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        add_balloon_talk(spawnId=401, msg='$52000020_QD__MAIN_01__5$', duration=1000, delayTick=0)
        add_balloon_talk(spawnId=402, msg='$52000020_QD__MAIN_01__6$', duration=1000, delayTick=0)
        add_balloon_talk(spawnId=403, msg='$52000020_QD__MAIN_01__7$', duration=1000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Emotion_Angry_A')
        add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_01__8$', duration=2000, align='left')
        add_balloon_talk(spawnId=202, msg='$52000020_QD__MAIN_01__9$', duration=2000, delayTick=1000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return battle_ready()


#  전투 씬 
class battle_ready(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=False)
        set_sound(triggerId=7002, arg2=True)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[301]) # 연출용 흑성회 대장(11001262)
        destroy_monster(spawnIds=[401,402,403]) # 연출용 흑성회

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return battle()


class battle(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        create_monster(spawnIds=[501], arg2=True) # 몬스터 흑성회 대장
        create_monster(spawnIds=[601,602,603], arg2=True) # 몬스터 흑성회

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return battleMsg()


class battleMsg(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52000020_QD__MAIN_01__10$', arg3='3000', arg4='0')
        add_balloon_talk(spawnId=601, msg='$52000020_QD__MAIN_01__11$', duration=3000, delayTick=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[501,601,602,603]):
            return delay()


class delay(state.State):
    def on_enter(self):
        set_sound(triggerId=7002, arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return winready()


class winready(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202]) # 연출용 리퍼트
        destroy_monster(spawnIds=[501]) # 흑성회 대장
        destroy_monster(spawnIds=[601,602,603]) # 흑성회
        create_monster(spawnIds=[201], arg2=True) # 퀘스트용 리퍼트(11001262)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return end()


class end(state.State):
    pass


