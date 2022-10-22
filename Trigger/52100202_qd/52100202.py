""" trigger/52100202_qd/52100202.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003250], questStates=[2]):
            return wait_01_02()


class wait_01_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4001], returnView=False)
        set_cinematic_ui(type=1)
        move_user(mapId=52100202, portalId=6001)
        set_mesh(triggerIds=[4026], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 티마이온()


class 티마이온(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 티마이온_02()


class 티마이온_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        set_cinematic_ui(type=3)
        move_user_path(patrolName='MS2PatrolData_3001')
        add_cinematic_talk(npcId=0, msg='$52100202_QD__52100202__0$', duration=3500)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 티마이온_03()


class 티마이온_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 티마이온_03_01()


class 티마이온_03_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        set_npc_emotion_loop(spawnId=101, sequenceName='Attack_Idle', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 티마이온_03_02()


class 티마이온_03_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_01_J')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 티마이온_04()


class 티마이온_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004,4006], returnView=False)
        face_emotion(spawnId=0, emotionName='Trigger_serious')
        add_cinematic_talk(npcId=0, msg='$52100202_QD__52100202__1$', duration=4500)
        add_cinematic_talk(npcId=0, msg='$52100202_QD__52100202__2$', duration=4500)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 정리_02()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정리_02()


class 정리_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정리_03()


class 정리_03(state.State):
    def on_enter(self):
        move_user(mapId=2020036, portalId=6001)


