""" trigger/52020030_qd/main30000332.xml """
import common


# 천공의 탑 입장
class 입장(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[30000332], questStates=[1]):
            return 천공의탑전경보여주기(self.ctx)


class 천공의탑전경보여주기(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 천공의탑전경보여주기02(self.ctx)


class 천공의탑전경보여주기02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[4008,4010], returnView=False)
        self.show_caption(type='VerticalCaption', title='천공의 탑', desc='크리티아스 마법 연구소', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 천공의탑전경보여주기03(self.ctx)


class 천공의탑전경보여주기03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52020030, portalId=6006)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 천공의탑전경보여주기04(self.ctx)


class 천공의탑전경보여주기04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 입장
