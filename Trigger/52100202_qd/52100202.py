""" trigger/52100202_qd/52100202.xml """
import common


class wait_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003250], questStates=[2]):
            return wait_01_02(self.ctx)


class wait_01_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52100202, portalId=6001)
        self.set_mesh(triggerIds=[4026], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 티마이온(self.ctx)


class 티마이온(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 티마이온_02(self.ctx)


class 티마이온_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrolName='MS2PatrolData_3001')
        self.add_cinematic_talk(npcId=0, msg='$52100202_QD__52100202__0$', duration=3500)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 티마이온_03(self.ctx)


class 티마이온_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 티마이온_03_01(self.ctx)


class 티마이온_03_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Attack_Idle', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 티마이온_03_02(self.ctx)


class 티마이온_03_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_01_J')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 티마이온_04(self.ctx)


class 티마이온_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004,4006], returnView=False)
        self.face_emotion(spawnId=0, emotionName='Trigger_serious')
        self.add_cinematic_talk(npcId=0, msg='$52100202_QD__52100202__1$', duration=4500)
        self.add_cinematic_talk(npcId=0, msg='$52100202_QD__52100202__2$', duration=4500)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 정리_02(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정리_02(self.ctx)


class 정리_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정리_03(self.ctx)


class 정리_03(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2020036, portalId=6001)


initial_state = wait_01
