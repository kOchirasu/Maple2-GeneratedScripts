""" trigger/52000102_qd/52000102.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9100]):
            return 입장01(self.ctx)


class 입장01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.create_monster(spawnIds=[200], animationEffect=False)
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.move_user_path(patrolName='MS2PatrolData_PC_Walk01')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 입장02(self.ctx)


class 입장02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4010,4011], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 입장03(self.ctx)


class 입장03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4012], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 입장04(self.ctx)


class 입장04(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait02(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52000102, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait02(self.ctx)


class Wait02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9100], questIds=[20002292], questStates=[3]):
            return PC화남01(self.ctx)


# ########################씬3 케이틀린과 대화퀘스트 이후########################
class PC화남01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=PC화남12, action='exit')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000102, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return PC화남02(self.ctx)


class PC화남02(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_Trun')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npcId=11003148, illustId='Anos_normal', msg='$52000102_QD__52000102__0$', duration=4000, align='right')
        self.select_camera_path(pathIds=[4000,4001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return PC화남03(self.ctx)


class PC화남03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003148, illustId='Anos_normal', msg='$52000102_QD__52000102__1$', duration=2000, align='right')
        self.set_sound(triggerId=9005, enable=True) # 케이틀린 대련 브금

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC화남04(self.ctx)


class PC화남04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52000102_QD__52000102__2$', duration=2000, align='right')
        self.face_emotion(spawnId=0, emotionName='PC_OutOfMind_01')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC화남04B(self.ctx)


class PC화남04B(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Dead_A'])
        self.face_emotion(spawnId=0, emotionName='PC_OutOfMind_01')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC화남05(self.ctx)


class PC화남05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52000102_QD__52000102__3$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return PC화남06(self.ctx)


class PC화남06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52000102_QD__52000102__4$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return PC화남08(self.ctx)


class PC화남08(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.add_cinematic_talk(npcId=11003149, illustId='Asimov_normal', msg='$52000102_QD__52000102__5$', duration=3000, align='right')
        self.face_emotion(spawnId=0, emotionName='ChaosMod_Start')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC화남09(self.ctx)


class PC화남09(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4006,4007], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52000102_QD__52000102__6$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC화남10(self.ctx)


class PC화남10(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return PC화남11(self.ctx)


class PC화남11(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.show_caption(type='VerticalCaption', title='$52000102_QD__52000102__7$', desc='$52000102_QD__52000102__8$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return PC화남11_1(self.ctx)


class PC화남11_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC화남12(self.ctx)


class PC화남12(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000115, portalId=1)


initial_state = Wait
