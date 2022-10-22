""" trigger/52000202_qd/52000202.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003431], questStates=[1]):
            return CameraEffect01()
        if not quest_user_detected(boxIds=[2001], questIds=[10003431], questStates=[1]):
            return 고마해_04()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        set_cinematic_ui(type=1)
        move_user(mapId=52000202, portalId=5001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_3()


class CameraEffect03_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3001')
        show_caption(type='VerticalCaption', title='$52000202_QD__52000202__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 시공의균열()


class 시공의균열(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003,4004], returnView=False)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__1$', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__2$', duration=5000)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__3$', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=14000):
            return 시공의균열_02_01()


class 시공의균열_02_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_long.xml')
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=11000)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__4$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시공의균열_02_02()


class 시공의균열_02_02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__5$', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__6$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 시공의균열_03()


class 시공의균열_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_long.xml')
        select_camera_path(pathIds=[4005], returnView=False)
        create_monster(spawnIds=[201])
        create_monster(spawnIds=[202])
        set_portal(portalId=8001, visible=False, enabled=False)
        set_portal(portalId=8002, visible=False, enabled=False)
        move_user(mapId=52000202, portalId=5002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 시공의균열_03_02()


class 시공의균열_03_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006], returnView=False)
        create_monster(spawnIds=[203])
        create_monster(spawnIds=[204])
        set_portal(portalId=8003, visible=False, enabled=False)
        set_portal(portalId=8004, visible=False, enabled=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 시공의균열_04()


class 시공의균열_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007,4008], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__7$', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__8$', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 전투준비()


class 전투준비(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=4500)
        select_camera_path(pathIds=[4009], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__9$', duration=4500)
        destroy_monster(spawnIds=[201])
        destroy_monster(spawnIds=[202])
        destroy_monster(spawnIds=[203])
        destroy_monster(spawnIds=[204])
        create_monster(spawnIds=[205])
        create_monster(spawnIds=[206])
        create_monster(spawnIds=[207])
        create_monster(spawnIds=[208])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return UI테스트()


class UI테스트(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 몰려온다()


class 몰려온다(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3006') # 뛰어가기
        move_npc(spawnId=205, patrolName='MS2PatrolData_3002')
        move_npc(spawnId=206, patrolName='MS2PatrolData_3003')
        move_npc(spawnId=207, patrolName='MS2PatrolData_3004')
        move_npc(spawnId=208, patrolName='MS2PatrolData_3005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몰려온다_02()


class 몰려온다_02(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=0.1, endScale=0.5, duration=5, interpolator=1)
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 몰려온다_03()


class 몰려온다_03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[205])
        destroy_monster(spawnIds=[206])
        destroy_monster(spawnIds=[207])
        destroy_monster(spawnIds=[208])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 고마해()


class 고마해(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        set_cinematic_ui(type=1)
        select_camera_path(pathIds=[4011], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 고마해_02()


class 고마해_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__10$', duration=2500)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__11$', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__12$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9500):
            return 고마해_03()


class 고마해_03(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=9000)
        set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_long.xml')
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__13$', duration=4500)
        add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__14$', duration=4000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8500):
            return 고마해_04()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 고마해_04()


class 고마해_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_achievement(triggerId=2001, achieve='illusionaryAttack')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 이동시키기()


class 이동시키기(state.State):
    def on_enter(self):
        move_user(mapId=52000201, portalId=5001)


