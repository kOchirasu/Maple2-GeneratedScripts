""" trigger/52000198_qd/52000198.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        set_portal(portalId=5002, visible=False, enabled=False)
        set_portal(portalId=2, visible=False, enabled=False)
        set_portal(portalId=4, visible=False, enabled=False)
        set_mesh(triggerIds=[8002], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003422], questStates=[2]):
            return 도망쳐_12()
        if quest_user_detected(boxIds=[2001], questIds=[10003422], questStates=[1]):
            return CameraEffect01()
        if quest_user_detected(boxIds=[2001], questIds=[10003422], questStates=[3]):
            return 도망쳐_26()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101]) # 에레브
        set_cinematic_ui(type=1)
        move_user(mapId=52000198, portalId=5001)
        select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect04()


class CameraEffect04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 도망쳐_01()


class 도망쳐_01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=3)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__0$', duration=4000)
        add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__1$', align='left', illustId='Ereb_serious', duration=4500)
        add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__2$', duration=4000)
        add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__3$', align='left', illustId='Ereb_serious', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=17000):
            return 도망쳐_01_02()


class 도망쳐_01_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__4$', duration=4000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 도망쳐_02()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 도망쳐_02()


class 도망쳐_02(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='$52000198_QD__52000198__5$', duration=4000)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=101, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2002]):
            return 도망쳐_03()


class 도망쳐_03(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True)
        create_monster(spawnIds=[102]) # 에레브
        destroy_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2003]):
            return 도망쳐_04()


class 도망쳐_04(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=102, msg='$52000198_QD__52000198__6$', duration=4000)
        move_npc(spawnId=102, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2004]):
            return 도망쳐_05()


class 도망쳐_05(state.State):
    def on_enter(self):
        set_portal(portalId=4, visible=True, enabled=True)
        create_monster(spawnIds=[103]) # 에레브
        destroy_monster(spawnIds=[102])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2005]):
            return 도망쳐_06()


class 도망쳐_06(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=103, msg='$52000198_QD__52000198__7$', duration=4000)
        move_npc(spawnId=103, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2006]):
            return 도망쳐_07()


class 도망쳐_07(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 도망쳐_08()


class 도망쳐_08(state.State):
    def on_enter(self):
        move_user(mapId=52000198, portalId=5003)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 도망쳐_09()


class 도망쳐_09(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_2, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 도망쳐_10()


class 도망쳐_10(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__8$', align='right', illustId='Ereb_serious', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 도망쳐_10_01()


class 도망쳐_10_01(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__9$', duration=4000)
        add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__10$', align='right', illustId='Ereb_serious', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8500):
            return 도망쳐_10_02()


class 도망쳐_10_02(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Talk_A', duration=4500)
        add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__11$', duration=4500)
        add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__12$', align='right', illustId='Ereb_closeEye', duration=1800)
        add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__13$', align='right', illustId='Ereb_serious', duration=4500)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10800):
            return 도망쳐_11()


class Skip_2(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 도망쳐_11()


class 도망쳐_11(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=103, msg='$52000198_QD__52000198__14$', duration=4000)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2007], questIds=[10003422], questStates=[2]):
            return 도망쳐_12()


class 도망쳐_12(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 도망쳐_13()


class 도망쳐_13(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104]) # 바론
        move_user(mapId=52000198, portalId=5004)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 도망쳐_14()


class 도망쳐_14(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_3, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 도망쳐_15()


class 도망쳐_15(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__15$', duration=4000)
        add_cinematic_talk(npcId=11004787, msg='$52000198_QD__52000198__16$', align='left', illustId='Baron_normal', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8500):
            return 도망쳐_15_01()


class 도망쳐_15_01(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__17$', duration=4500)
        add_cinematic_talk(npcId=11004787, msg='$52000198_QD__52000198__18$', align='left', illustId='Baron_normal', duration=4000)
        add_cinematic_talk(npcId=11004787, msg='$52000198_QD__52000198__19$', align='left', illustId='Baron_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12500):
            return 도망쳐_16()


class 도망쳐_16(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 도망쳐_17()


class 도망쳐_17(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104]) # 아래층바론
        create_monster(spawnIds=[105]) # 바론
        move_user(mapId=52000198, portalId=5003)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 도망쳐_19()


class 도망쳐_19(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 도망쳐_20()


class 도망쳐_20(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__20$', align='right', illustId='Ereb_surprise', duration=4000)
        add_cinematic_talk(npcId=11004787, msg='$52000198_QD__52000198__21$', align='left', illustId='Baron_normal', duration=4000)
        add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__22$', align='right', illustId='Ereb_serious', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12500):
            return 도망쳐_21()


class 도망쳐_21(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_3004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 도망쳐_22()


class 도망쳐_22(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Object_React_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 도망쳐_23()


class 도망쳐_23(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        set_mesh(triggerIds=[8001], visible=False)
        set_mesh(triggerIds=[8002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 도망쳐_24()


class 도망쳐_24(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        reset_camera(interpolationTime=0)
        add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__23$', align='right', illustId='Ereb_serious', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 도망쳐_25()


class Skip_3(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[104]) # 아래층바론
        destroy_monster(spawnIds=[105])
        create_monster(spawnIds=[105]) # 바론
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_mesh(triggerIds=[8001], visible=False)
        set_mesh(triggerIds=[8002], visible=True)
        move_user(mapId=52000198, portalId=5003)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 도망쳐_25()


class 도망쳐_25(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        destroy_monster(spawnIds=[103])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003422], questStates=[3]):
            return 도망쳐_26()


class 도망쳐_26(state.State):
    def on_enter(self):
        set_portal(portalId=5002, visible=True, enabled=True) # 불길 속으로 퀘스트 바론에게 완료하고 나면 포탈이 활성화 되게 수정
        destroy_monster(spawnIds=[105])


