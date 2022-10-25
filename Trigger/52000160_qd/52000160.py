""" trigger/52000160_qd/52000160.xml """
import common


class wait_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002742], questStates=[3]):
            return 떠난다_01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002743], questStates=[3]):
            return 프론티아재단으로_01(self.ctx)
        if self.user_detected(boxIds=[2001], jobCode=0):
            return 전직컷씬01(self.ctx)


class 전직컷씬01(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='jobChange_Assassin.swf', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 다크윈드도착_01(self.ctx)
        if self.wait_tick(waitTick=8000):
            return 다크윈드도착_01(self.ctx)


class 다크윈드도착_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 다크윈드도착_02(self.ctx)


class 다크윈드도착_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 다크윈드도착_03(self.ctx)


class 다크윈드도착_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 다크윈드도착_04(self.ctx)


class 다크윈드도착_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001,4002], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 다크윈드도착_05(self.ctx)


class 다크윈드도착_05(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 다크윈드도착_06(self.ctx)


class 다크윈드도착_06(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 다크윈드도착_07(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 다크윈드도착_07(self.ctx)


class 다크윈드도착_07(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전직한다(self.ctx)


class 전직한다(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002742], questStates=[2]):
            return 전직이펙트_01(self.ctx)


class 전직이펙트_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전직이펙트_02(self.ctx)


class 전직이펙트_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 떠난다_01(self.ctx)


class 떠난다_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002743], questStates=[3]):
            return 프론티아재단으로_01(self.ctx)


class 프론티아재단으로_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 프론티아재단으로_02(self.ctx)


class 프론티아재단으로_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000186, portalId=1)


initial_state = wait_01
