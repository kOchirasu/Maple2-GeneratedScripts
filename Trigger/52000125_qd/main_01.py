""" trigger/52000125_qd/main_01.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100190,60100191,60100192,60100193,60100194,60100195], questStates=[2]):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_01()


#  씬 진행 
class scene_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4006], returnView=False)
        create_monster(spawnIds=[201], arg2=True) # 연출 제타 (11003207)
        move_user(mapId=52000125, portalId=6001)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Clap_A')
        add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN_01__0$', duration=3000, align='center')
        set_scene_skip(state=scene_08, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='ChatUp')
        add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN_01__1$', duration=1000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003208, msg='$52000125_QD__MAIN_01__2$', duration=2000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN_01__3$', duration=3000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003,4004,4005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_08()


class scene_08(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201]) # 연출용 제타()
        create_monster(spawnIds=[202], arg2=True) # 퀘스트용 제타 ()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return end()


class end(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100195], questStates=[2]):
            return eventtalk_start()


#  마크&제타 재회 
class eventtalk_start(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return eventtalk_01()


class eventtalk_01(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_3003')
        move_npc(spawnId=202, patrolName='MS2PatrolData_3004')
        add_balloon_talk(spawnId=102, msg='$52000125_QD__MAIN_01__4$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return eventtalk_02()


class eventtalk_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=202, sequenceName='ChatUp_A')
        add_balloon_talk(spawnId=202, msg='$52000125_QD__MAIN_01__5$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return eventtalk_03()


class eventtalk_03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=202, sequenceName='Talk_A')
        add_balloon_talk(spawnId=202, msg='$52000125_QD__MAIN_01__6$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return eventtalk_04()


class eventtalk_04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=202, sequenceName='ChatUp_A')
        add_balloon_talk(spawnId=202, msg='$52000125_QD__MAIN_01__7$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return eventtalk_05()


class eventtalk_05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Idle_A')
        add_balloon_talk(spawnId=102, msg='$52000125_QD__MAIN_01__8$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return eventtalk_06()


class eventtalk_06(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=202, sequenceName='Idle_A')
        add_balloon_talk(spawnId=202, msg='$52000125_QD__MAIN_01__9$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return eventtalk_02()


