""" trigger/52010066_qd/main.xml """
import common


class 연출01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            self.visible_my_pc(isVisible=False)
            self.set_mesh_animation(triggerIds=[9002], visible=False, arg3=0, arg4=0)
            self.set_cinematic_ui(type=1)
            return 연출02(self.ctx)


class 연출02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출03(self.ctx)


class 연출03(common.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=True, startScale=0.8, endScale=0.8, duration=8, interpolator=1) # 2초간 느려지기 시작
        self.select_camera_path(pathIds=[2000,2001,2002,2003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출04_b(self.ctx)


class 연출04_b(common.Trigger):
    def on_enter(self):
        self.set_mesh_animation(triggerIds=[9002], visible=True, arg3=0, arg4=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6800):
            return 연출04(self.ctx)


class 연출04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return quit(self.ctx)


class quit(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000422, portalId=3)


initial_state = 연출01
