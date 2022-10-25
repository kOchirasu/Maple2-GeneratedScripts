""" trigger/52010051_qd/darkmoonmovie.xml """
import common


class start(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return CameraEffect01(self.ctx)


class CameraEffect01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect02(self.ctx)


class CameraEffect02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03(self.ctx)


class CameraEffect03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera(triggerId=1000, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect4(self.ctx)


class CameraEffect4(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=1001, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return CameraEffect5(self.ctx)


class CameraEffect5(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=99999890, portalId=0)


initial_state = start
