""" trigger/52000200_qd/52000200.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001]):
            return CameraEffect01()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_enter(self):
        set_quest_accept(questId=10003419) # 퀘스트 강제 수락
        select_camera_path(pathIds=[4001], returnView=False)
        visible_my_pc(isVisible=False) # 유저 투명 처리
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[101]) # 바론
        create_monster(spawnIds=[102]) # 칼
        create_monster(spawnIds=[103]) # 에레브

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect02_02()


class CameraEffect02_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000200_QD__52000200__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=1)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_3()


class CameraEffect03_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4003], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 여제알현()


class 여제알현(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__1$', illustId='Ereb_normal', align='left', duration=4000)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__2$', align='right', illustId='Karl_normal', duration=4000)
        add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__3$', illustId='Ereb_normal', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 여제알현_02()


class 여제알현_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004,4005], returnView=False)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__4$', align='right', illustId='Karl_normal', duration=4000)
        add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__5$', illustId='Ereb_normal', align='left', duration=4500)
        add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__6$', illustId='Ereb_normal', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11500):
            return 여제알현_03()


class 여제알현_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__7$', align='right', illustId='Karl_normal', duration=4000)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__8$', align='right', illustId='Karl_normal', duration=4000)
        add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__9$', illustId='Ereb_surprise', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return 여제알현_04()


class 여제알현_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_3002')
        move_npc(spawnId=103, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 여제알현_05()


class 여제알현_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004782, msg='$52000200_QD__52000200__10$', align='left', illustId='Ruana_normal', duration=4000)
        add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__11$', align='left', illustId='Ereb_surprise', duration=4000)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__12$', align='right', illustId='Karl_normal', duration=4500)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__13$', align='right', illustId='Karl_normal', duration=4500)
        add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__14$', align='left', illustId='Ereb_surprise', duration=3000)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__15$', align='right', illustId='Karl_normal', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return 여제알현_06()


class 여제알현_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007,4008], returnView=False)
        add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__16$', align='left', illustId='Ereb_surprise', duration=4500)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__17$', align='right', illustId='Karl_normal', duration=2800)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__18$', align='right', illustId='Karl_normal', duration=4500)
        add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__19$', align='left', illustId='Ereb_surprise', duration=4000)
        add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__20$', align='left', illustId='Ereb_closeEye', duration=4000)
        add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__21$', align='left', illustId='Ereb_closeEye', duration=4000)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__22$', align='right', illustId='Karl_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=27800):
            return 음모()


class 음모(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 음모_02()


class 음모_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000200_QD__52000200__23$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 음모_03()


class 음모_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11001975, msg='$52000200_QD__52000200__24$', align='left', duration=4500)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__25$', align='right', illustId='Karl_normal', duration=2800)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__26$', align='right', illustId='Karl_normal', duration=4000)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__27$', align='right', illustId='Karl_normal', duration=3000)
        add_cinematic_talk(npcId=11000264, msg='$52000200_QD__52000200__28$', align='left', illustId='Radin_normal', duration=4500)
        add_cinematic_talk(npcId=11000264, msg='$52000200_QD__52000200__29$', align='left', illustId='Radin_normal', duration=4000)
        add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__30$', align='right', illustId='Karl_normal', duration=4000)
        add_cinematic_talk(npcId=11000264, msg='$52000200_QD__52000200__31$', align='left', illustId='Radin_normal', duration=4000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=29000):
            return 이동()


class Skip_1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True) # 유저 투명 처리
        move_user(mapId=52000190, portalId=5001)


