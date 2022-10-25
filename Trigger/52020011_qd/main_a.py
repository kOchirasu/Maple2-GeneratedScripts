""" trigger/52020011_qd/main_a.xml """
import common


class Idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200015], questStates=[2]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Setting(self.ctx)


class Setting(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.move_user(mapId=52020011, portalId=6001)
        self.set_scene_skip(state=Exit, action='Exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_01(self.ctx)


class scene_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.show_caption(type='VerticalCaption', title='$map:52020011$', desc='$NpcName:11003599$의 임시 거처', align='centerLeft', offsetRateX=0.05, offsetRateY=0.15, duration=3000, scale=1.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return scene_02(self.ctx)


class scene_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003,4004,4005,4006], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return scene_03(self.ctx)

    def on_exit(self):
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Chin_Chin_A'])


class scene_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4007,4008], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return scene_04(self.ctx)


class scene_04(common.Trigger):
    def on_enter(self):
        self.show_caption(type='NameCaption', title='$NpcName:11003599$', desc='크리티아스 왕녀', align='centerLeft', offsetRateX=0.05, offsetRateY=0.15, duration=3000, scale=2)
        self.add_cinematic_talk(npcId=11003599, msg='그래, 반갑구나.', duration=2800)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Exit(self.ctx)


class Exit(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)


initial_state = Idle
