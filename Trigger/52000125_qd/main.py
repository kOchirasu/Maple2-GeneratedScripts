""" trigger/52000125_qd/main.xml """
from common import *
import state


# 노란 머리의 행방: 60100185 / 거짓말의 이유: 60100190 / 유력한 목격자: 60100195 
class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True) # 연출용 마크(11003205)
        set_sound(triggerId=7001, arg2=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100185], questStates=[1]):
            return fadein()
        if quest_user_detected(boxIds=[2001], questIds=[60100185,60100186,60100187,60100188,60100189,60100190,60100191,60100192,60100193,60100194,60100195], questStates=[2]):
            return end()


#  준비 
class fadein(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_scene_skip(state=battle_ready, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ready()


class ready(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        create_monster(spawnIds=[301], arg2=True) # 연출용 디나(11003214)
        create_monster(spawnIds=[302], arg2=True)
        create_monster(spawnIds=[303], arg2=True) # 연출용 디오(11003212)
        move_user(mapId=52000125, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start()


class start(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_01()


#  이벤트 씬 시작 
class scene_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN__0$', duration=3000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        add_cinematic_talk(npcId=11003214, msg='$52000125_QD__MAIN__1$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003214, msg='$52000125_QD__MAIN__2$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        add_cinematic_talk(npcId=11003213, msg='$52000125_QD__MAIN__3$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN__4$', duration=3000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010], returnView=False)
        add_cinematic_talk(npcId=11003212, msg='$52000125_QD__MAIN__5$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_08()


class scene_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN__6$', duration=3000, align='center')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return battle_ready()


#  전투 씬 
class battle_ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return wait()


class wait(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[301,302,303]) # 연출용 마스크단
        create_monster(spawnIds=[601,602,603], arg2=False) # 몬스터 불량배
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return battle()


class battle(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_balloon_talk(spawnId=601, msg='$52000125_QD__MAIN__7$', duration=3000, delayTick=1000)
        add_balloon_talk(spawnId=602, msg='$52000125_QD__MAIN__8$', duration=3000, delayTick=3000)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return battleMsg()


class battleMsg(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52000125_QD__MAIN__9$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,602,603]):
            return delay()


class delay(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_achievement(triggerId=2001, type='trigger', achieve='markguard')
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return winready()


class winready(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[601,602,603]) # 불량배
        create_monster(spawnIds=[304,305,306], arg2=True)
        move_user(mapId=52000125, portalId=6001)
        select_camera_path(pathIds=[4005], returnView=False)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_scene_skip(state=end, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return endcamera()


class endcamera(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return bye()


class bye(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003214, msg='$52000125_QD__MAIN__10$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return run()


class run(state.State):
    def on_enter(self):
        move_npc(spawnId=304, patrolName='MS2PatrolData_3002')
        move_npc(spawnId=305, patrolName='MS2PatrolData_3002')
        move_npc(spawnId=306, patrolName='MS2PatrolData_3002')
        add_cinematic_talk(npcId=11003214, msg='$52000125_QD__MAIN__11$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return thanks()


class thanks(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Clap_A')
        add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN__12$', duration=2000, align='center')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return end()


class end(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_sound(triggerId=7001, arg2=False)
        destroy_monster(spawnIds=[304,305,306])
        destroy_monster(spawnIds=[101]) # 연출용 마크(11003205)
        create_monster(spawnIds=[102], arg2=True) # 퀘스트용 마크(11003206)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)


