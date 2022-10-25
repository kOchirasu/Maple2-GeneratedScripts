""" trigger/52000199_qd/52000199_2.xml """
import common


class start(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003448], questStates=[2]):
            return CameraEffect01(self.ctx)


class CameraEffect01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user(mapId=52000199, portalId=5001)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraEffect02(self.ctx)


class CameraEffect02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000199_QD__52000199_2__0$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return CameraEffect02_2(self.ctx)


class CameraEffect02_2(common.Trigger):
    def on_enter(self):
        self.set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'], visible=False)
        self.add_buff(boxIds=[2001], skillId=99910403, level=1, isPlayer=False, isSkillSet=True) # 다크로드 변신
        self.add_buff(boxIds=[2001], skillId=99910403, level=1, isPlayer=False, isSkillSet=False) # 다크로드 변신

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03(self.ctx)


class CameraEffect03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = start
