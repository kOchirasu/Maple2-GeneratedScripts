""" trigger/52000194_qd/52000194.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003427], questStates=[2]):
            return Wait_02(self.ctx)


class Wait_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000194, portalId=5001)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 영상재생(self.ctx)


class 영상재생(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='common\unconsciousEmpress.usm', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 시공의균열(self.ctx)
        if self.wait_tick(waitTick=30000):
            return 시공의균열(self.ctx)


class 시공의균열(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 시공의균열_02(self.ctx)


class 시공의균열_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001,4002], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52000194_QD__52000194__0$', desc='$52000194_QD__52000194__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시공의균열_03(self.ctx)


class 시공의균열_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 시공의균열_04(self.ctx)


class 시공의균열_04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = Wait
