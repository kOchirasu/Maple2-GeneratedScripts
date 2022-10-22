""" trigger/52100109_qd/main.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[91000980], questStates=[1]):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_cinematic_ui(type=1)
        move_user(mapId=52100109, portalId=2)
        visible_my_pc(isVisible=False)
        create_monster(spawnIds=[101])
        create_monster(spawnIds=[102])
        create_monster(spawnIds=[103])
        select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_npc(spawnId=102, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 삼자대면()


class 삼자대면(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005,4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 삼자대면_02()


class 삼자대면_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=5000)
        add_cinematic_talk(npcId=11004614, msg='$52100109_QD__MAIN__0$', align='left', illustId='Eone_normal', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 삼자대면_02_01()


class 삼자대면_02_01(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=8500)
        add_cinematic_talk(npcId=11004616, msg='$52100109_QD__MAIN__1$', align='right', illustId='Bliche_closeEye', duration=4500)
        add_cinematic_talk(npcId=11004616, msg='$52100109_QD__MAIN__2$', align='right', illustId='Bliche_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8500):
            return 삼자대면_02_02()


class 삼자대면_02_02(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=9000)
        add_cinematic_talk(npcId=11004614, msg='$52100109_QD__MAIN__3$', align='left', illustId='Eone_normal', duration=4000)
        add_cinematic_talk(npcId=11004614, msg='$52100109_QD__MAIN__4$', align='left', illustId='Eone_serious', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 삼자대면_02_03()


class 삼자대면_02_03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=5200)
        add_cinematic_talk(npcId=11004616, msg='$52100109_QD__MAIN__5$', align='right', illustId='Bliche_normal', duration=2000)
        add_cinematic_talk(npcId=11004616, msg='$52100109_QD__MAIN__6$', align='right', illustId='Bliche_normal', duration=3200)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5200):
            return 삼자대면_02_04()


class 삼자대면_02_04(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3200)
        add_cinematic_talk(npcId=11004614, msg='$52100109_QD__MAIN__7$', align='left', illustId='Eone_closeEye', duration=3200)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3200):
            return 삼자대면_03()


class 삼자대면_03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=19000)
        select_camera_path(pathIds=[4003], returnView=False)
        add_cinematic_talk(npcId=11004615, msg='$52100109_QD__MAIN__8$', align='left', illustId='siman_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 삼자대면_03_00()


class 삼자대면_03_00(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=11004615, msg='$52100109_QD__MAIN__9$', align='left', illustId='siman_normal', duration=5000)
        add_cinematic_talk(npcId=11004615, msg='$52100109_QD__MAIN__10$', align='left', illustId='siman_normal', duration=5000)
        add_cinematic_talk(npcId=11004615, msg='$52100109_QD__MAIN__11$', align='left', illustId='siman_normal', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 삼자대면_03_01()


class 삼자대면_03_01(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=5000)
        add_cinematic_talk(npcId=11004614, msg='$52100109_QD__MAIN__12$', align='left', illustId='Eone_serious', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 삼자대면_03_02()


class 삼자대면_03_02(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=4500)
        add_cinematic_talk(npcId=11004616, msg='$52100109_QD__MAIN__13$', align='right', illustId='Bliche_closeEye', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 삼자대면_03_03()


class 삼자대면_03_03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=8500)
        add_cinematic_talk(npcId=11004614, msg='$52100109_QD__MAIN__14$', align='left', illustId='Eone_normal', duration=4000)
        add_cinematic_talk(npcId=11004614, msg='$52100109_QD__MAIN__15$', align='left', illustId='Eone_closeEye', duration=4500)
        add_cinematic_talk(npcId=11004616, msg='$52100109_QD__MAIN__16$', align='right', illustId='Bliche_closeEye', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11300):
            return 삼자대면_03_04()


class 삼자대면_03_04(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=4500)
        add_cinematic_talk(npcId=11004616, msg='$52100109_QD__MAIN__17$', align='right', illustId='Bliche_normal', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 삼자대면_04()


class 삼자대면_04(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3200)
        add_cinematic_talk(npcId=11004614, msg='$52100109_QD__MAIN__18$', align='left', illustId='Eone_normal', duration=3200)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3200):
            return 삼자대면_04_01()


class 삼자대면_04_01(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=4500)
        add_cinematic_talk(npcId=11004616, msg='$52100109_QD__MAIN__19$', align='right', illustId='Bliche_normal', duration=4500)
        add_cinematic_talk(npcId=11004615, msg='$52100109_QD__MAIN__20$', align='left', illustId='siman_normal', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 삼자대면_04_02()


class 삼자대면_04_02(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=8000)
        add_cinematic_talk(npcId=11004614, msg='$52100109_QD__MAIN__21$', align='left', illustId='Eone_smile', duration=4000)
        add_cinematic_talk(npcId=11004615, msg='$52100109_QD__MAIN__22$', align='right', illustId='siman_normal', duration=4000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 삼자대면끝()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정리()


class 삼자대면끝(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정리()


class 정리(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        visible_my_pc(isVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 정리_02()


class 정리_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=2001, achieve='Georg')


