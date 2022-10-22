""" trigger/52020011_qd/main_a.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200015], questStates=[2]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Setting()


class Setting(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera_path(pathIds=[4001], returnView=False)
        move_user(mapId=52020011, portalId=6001)
        set_scene_skip(state=Exit, arg2='Exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return scene_01()


class scene_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4002], returnView=False)
        show_caption(type='VerticalCaption', title='$map:52020011$', desc='$NpcName:11003599$의 임시 거처', align='centerLeft', offsetRateX=0.05, offsetRateY=0.15, duration=3000, scale=1.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003,4004,4005,4006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return scene_03()

    def on_exit(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Chin_Chin_A'])


class scene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007,4008], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        show_caption(type='NameCaption', title='$NpcName:11003599$', desc='크리티아스 왕녀', align='centerLeft', offsetRateX=0.05, offsetRateY=0.15, duration=3000, scale=2)
        add_cinematic_talk(npcId=11003599, msg='그래, 반갑구나.', duration=2800)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Exit()


class Exit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)


