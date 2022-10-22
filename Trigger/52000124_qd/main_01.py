""" trigger/52000124_qd/main_01.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100145], questStates=[1]):
            return ready()
        if quest_user_detected(boxIds=[2001], questIds=[60100145,60100146,60100147,60100148,60100149,60100150], questStates=[2]):
            return delay()


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52000124, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_01()


#  씬 진행 
class scene_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4001,4002], returnView=False)
        create_monster(spawnIds=[401,402], arg2=True) # 레논 추종자
        add_cinematic_talk(npcId=11000069, msg='$52000124_QD__MAIN_01__0$', duration=2000, align='left')
        set_scene_skip(state=battle_ready, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000069, msg='$52000124_QD__MAIN_01__1$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=True)
        add_cinematic_talk(npcId=11003304, msg='$52000124_QD__MAIN_01__2$', duration=2000, align='left')
        add_balloon_talk(spawnId=101, msg='$52000124_QD__MAIN_01__3$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003304, msg='$52000124_QD__MAIN_01__4$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000069, msg='$52000124_QD__MAIN_01__5$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003304, msg='$52000124_QD__MAIN_01__6$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_08()


class scene_08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003304, msg='$52000124_QD__MAIN_01__7$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return battle_ready()


#  전투 씬 
class battle_ready(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[401,402]) # 레논 추종자

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return battle()


class battle(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        create_monster(spawnIds=[601,602], arg2=True) # 레논 추종자

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return battleMsg()


class battleMsg(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52000124_QD__MAIN_01__8$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,602]):
            return delay()


class delay(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_achievement(triggerId=2001, type='trigger', achieve='eveguard')
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return winready()


class winready(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[601,602]) # 연출용 마크(11003205)
        move_user(mapId=52000124, portalId=6001)
        create_monster(spawnIds=[302], arg2=True) # 연출용 카트반

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_09()


#  전투 종료 
class scene_09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_10()


class scene_10(state.State):
    def on_enter(self):
        move_npc(spawnId=302, patrolName='MS2PatrolData_3002')
        select_camera_path(pathIds=[4007,4008], returnView=False)
        add_cinematic_talk(npcId=11003196, illustId='Katvan_normal', msg='$52000124_QD__MAIN_01__9$', duration=3000, align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_11()


class scene_11(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[302]) # 연출용 카트반
        create_monster(spawnIds=[301], arg2=True) # 퀘스트 카트반

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return end()


class end(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


#  카트반 제거 종료 
class del(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])


