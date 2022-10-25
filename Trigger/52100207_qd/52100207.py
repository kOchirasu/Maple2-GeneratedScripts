""" trigger/52100207_qd/52100207.xml """
import common


class wait_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003190], questStates=[2]):
            return wait_01_02(self.ctx)


class wait_01_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 요랑의방_01(self.ctx)


class 요랑의방_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 요랑의방_02(self.ctx)


class 요랑의방_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=0, msg='$52100207_QD__52100207__0$', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 요랑의방_04(self.ctx)


class 요랑의방_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52100207_QD__52100207__1$', duration=2500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 요랑의방_05(self.ctx)


class 요랑의방_05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52100207_QD__52100207__2$', duration=1500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 요랑의방_06(self.ctx)


class 요랑의방_06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52100207_QD__52100207__3$', duration=3000)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 정리_01(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정리_01(self.ctx)


class 정리_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 정리_02(self.ctx)


class 정리_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = wait_01
