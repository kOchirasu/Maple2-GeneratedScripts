""" trigger/52000199_qd/52000199.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2001], jobCode=0):
            return 이동(self.ctx)


class 이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000199, portalId=5001)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003416], questStates=[2]):
            return CameraEffect01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[10003417], questStates=[1]):
            return Wait_02(self.ctx)


class CameraEffect01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect02(self.ctx)


class CameraEffect02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03(self.ctx)


class CameraEffect03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03_3(self.ctx)


class CameraEffect03_3(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52000199_QD__52000199__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return CameraEffect04(self.ctx)


class CameraEffect04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect05(self.ctx)


class CameraEffect05(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003417], questStates=[1]):
            return Wait_02(self.ctx)


class Wait_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 영상재생(self.ctx)


class 영상재생(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='common\KiliansTruth.usm', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 바깥으로(self.ctx)
        if self.wait_tick(waitTick=203000):
            return 바깥으로(self.ctx)


class 바깥으로(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        self.set_achievement(triggerId=2001, achieve='KiliansTruth')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 바깥으로_02(self.ctx)


class 바깥으로_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000146, portalId=12)


initial_state = Wait
