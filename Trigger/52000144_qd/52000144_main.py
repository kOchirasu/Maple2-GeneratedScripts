""" trigger/52000144_qd/52000144_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return 잠시대기_01()


class 잠시대기_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 잠시대기_02()


class 잠시대기_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 입장_01()


class 입장_01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 입장_02()


class 입장_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 로베와대화_01()


class 로베와대화_01(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Knight_Bore_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 로베와대화_02()


class 로베와대화_02(state.State):
    def on_enter(self):
        set_scene_skip(state=스킵도착_01, arg2='exit')
        add_cinematic_talk(npcId=0, msg='$52000144_QD__52000144_MAIN__0$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 로베와대화_03()


class 로베와대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003401, msg='$52000144_QD__52000144_MAIN__1$', duration=3000, illustId='Robe_normal', align='right')
        add_cinematic_talk(npcId=11003401, msg='$52000144_QD__52000144_MAIN__2$', duration=3500, illustId='Robe_normal', align='right')
        add_cinematic_talk(npcId=11003401, msg='$52000144_QD__52000144_MAIN__3$', duration=3500, illustId='Robe_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 로베와대화_04()


class 로베와대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000144_QD__52000144_MAIN__4$', duration=4179, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 로베와대화_05()


class 로베와대화_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003401, msg='$52000144_QD__52000144_MAIN__5$', duration=3000, illustId='Robe_normal', align='right')
        add_cinematic_talk(npcId=11003401, msg='$52000144_QD__52000144_MAIN__6$', duration=3500, illustId='Robe_normal', align='right')
        add_cinematic_talk(npcId=11003401, msg='$52000144_QD__52000144_MAIN__7$', duration=4000, illustId='Robe_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return 로베와대화_06()


class 로베와대화_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000144_QD__52000144_MAIN__8$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 로베와대화_06_1()


class 로베와대화_06_1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 로베와대화_07()


class 로베와대화_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003401, msg='$52000144_QD__52000144_MAIN__9$', duration=3000, illustId='Robe_normal', align='right')
        add_cinematic_talk(npcId=11003401, msg='$52000144_QD__52000144_MAIN__10$', duration=2500, illustId='Robe_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 로베와대화_08()


class 로베와대화_08(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Knight_Bore_A'])
        add_cinematic_talk(npcId=0, msg='$52000144_QD__52000144_MAIN__11$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 로베와대화_09()


class 로베와대화_09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마무리()


class 스킵도착_01(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마무리()


class 마무리(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=2000062, portalId=13)


