""" trigger/52000113_qd/52000113.xml """
from common import *
import state


class START(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10011]):
            return 대기01()


class 대기01(state.State):
    def on_enter(self):
        set_scene_skip(state=Quit02, arg2='exit')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        spawn_npc_range(rangeIds=[202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221], isAutoTargeting=False)
        create_monster(spawnIds=[101], arg2=False) # 쉐도우클로
        set_cinematic_ui(type=1)
        move_npc(spawnId=203, patrolName='MS2PatrolData_203') # 로그스들 이동
        move_npc(spawnId=204, patrolName='MS2PatrolData_204') # 로그스들 이동
        move_npc(spawnId=215, patrolName='MS2PatrolData_215') # 로그스들 이동
        move_npc(spawnId=216, patrolName='MS2PatrolData_216') # 로그스들 이동
        move_npc(spawnId=217, patrolName='MS2PatrolData_217') # 로그스들 이동
        move_npc(spawnId=219, patrolName='MS2PatrolData_219') # 로그스들 이동
        move_npc(spawnId=220, patrolName='MS2PatrolData_220') # 로그스들 이동
        move_npc(spawnId=221, patrolName='MS2PatrolData_221') # 로그스들 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return camera01()


class camera01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[1000,1001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return camera02()


class camera02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1002,1003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return camera03()


class camera03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1004,1005], returnView=False)
        move_npc(spawnId=208, patrolName='MS2PatrolData_Rogues_come') # 로그스들 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return camera04()


class camera04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1006,1007], returnView=False)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003338, illustId='0', msg='$52000113_QD__52000113__0$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return camera05()


class camera05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1008,1009], returnView=False)
        add_cinematic_talk(npcId=11003185, illustId='0', msg='$52000113_QD__52000113__1$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return camera06()


class camera06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1010], returnView=False)
        add_cinematic_talk(npcId=11003185, illustId='0', msg='$52000113_QD__52000113__2$', duration=4000, align='right')
        move_npc(spawnId=208, patrolName='MS2PatrolData_Rogues_out') # 로그스들 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return camera07()


class camera07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1011,1012], returnView=False)
        add_cinematic_talk(npcId=11003185, illustId='0', msg='$52000113_QD__52000113__3$', duration=5000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return camera08()


class camera08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003185, illustId='0', msg='$52000113_QD__52000113__4$', duration=5000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit01()


class Quit01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit01_1()


class Quit01_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_user(mapId=2000062, portalId=13)


