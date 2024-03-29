""" trigger/52010067_qd/main.xml """
import trigger_api


class 연출01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            self.visible_my_pc(isVisible=False)
            self.set_cinematic_ui(type=1)
            self.set_effect(triggerIds=[9010], visible=False)
            return 연출브릿지(self.ctx)


class 연출브릿지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[700], questIds=[20002290], questStates=[2]):
            return 조준씬01(self.ctx)
        if self.quest_user_detected(boxIds=[700], questIds=[20002290], questStates=[3]):
            return 피격씬01(self.ctx)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@포신정렬씬@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class 조준씬01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[200], animationEffect=False) # 인페르녹

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출02_b(self.ctx)


class 연출02_b(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1300):
            return 연출02_c(self.ctx)


class 연출02_c(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000,2001,2002,2003,2004], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5300):
            return 연출03(self.ctx)


class 연출03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2005,2006,2007,2008,2009,2010,2011], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3200):
            return 연출04(self.ctx)


class 연출04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2012], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출05(self.ctx)


class 연출05(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return quit(self.ctx)


class quit(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000422, portalId=3)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@피격씬@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class 피격씬01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 피격씬01_a(self.ctx)


class 피격씬01_a(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1300):
            return 피격씬02(self.ctx)


class 피격씬02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[9010], visible=True)
        self.select_camera_path(pathIds=[3004,3005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 피격씬03_a(self.ctx)


class 피격씬03_a(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3000,3001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3900):
            return 피격씬03(self.ctx)


class 피격씬03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3002,3003], returnView=False)
        self.set_time_scale(enable=True, startScale=0.1, endScale=0.1, duration=3.5, interpolator=1) # 2초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3600):
            return 피격씬04(self.ctx)


class 피격씬04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return quit02(self.ctx)


class quit02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000422, portalId=3)


initial_state = 연출01
