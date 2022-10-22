""" trigger/52000102_qd/52000102.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return 입장01()


class 입장01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        create_monster(spawnIds=[200], arg2=False)
        create_monster(spawnIds=[202], arg2=False)
        set_cinematic_ui(type=1)
        move_user_path(patrolName='MS2PatrolData_PC_Walk01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 입장02()


class 입장02(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4010,4011], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 입장03()


class 입장03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4012], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 입장04()


class 입장04(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait02()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        move_user(mapId=52000102, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait02()


class Wait02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9100], questIds=[20002292], questStates=[3]):
            return PC화남01()


#  ########################씬3 케이틀린과 대화퀘스트 이후########################
class PC화남01(state.State):
    def on_enter(self):
        set_scene_skip(state=PC화남12, arg2='exit')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000102, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PC화남02()


class PC화남02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_Trun')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        add_cinematic_talk(npcId=11003148, illustId='Anos_normal', msg='$52000102_QD__52000102__0$', duration=4000, align='right')
        select_camera_path(pathIds=[4000,4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PC화남03()


class PC화남03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003148, illustId='Anos_normal', msg='$52000102_QD__52000102__1$', duration=2000, align='right')
        set_sound(triggerId=9005, arg2=True) # 케이틀린 대련 브금

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC화남04()


class PC화남04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52000102_QD__52000102__2$', duration=2000, align='right')
        face_emotion(spawnId=0, emotionName='PC_OutOfMind_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC화남04B()


class PC화남04B(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Dead_A'])
        face_emotion(spawnId=0, emotionName='PC_OutOfMind_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC화남05()


class PC화남05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52000102_QD__52000102__3$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PC화남06()


class PC화남06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52000102_QD__52000102__4$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PC화남08()


class PC화남08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=11003149, illustId='Asimov_normal', msg='$52000102_QD__52000102__5$', duration=3000, align='right')
        face_emotion(spawnId=0, emotionName='ChaosMod_Start')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC화남09()


class PC화남09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006,4007], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52000102_QD__52000102__6$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC화남10()


class PC화남10(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return PC화남11()


class PC화남11(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        show_caption(type='VerticalCaption', title='$52000102_QD__52000102__7$', desc='$52000102_QD__52000102__8$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PC화남11_1()


class PC화남11_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC화남12()


class PC화남12(state.State):
    def on_enter(self):
        move_user(mapId=52000115, portalId=1)


