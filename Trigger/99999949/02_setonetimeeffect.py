""" trigger/99999949/02_setonetimeeffect.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_black.xml')
        self.set_onetime_effect(id=2, enable=False, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        self.set_onetime_effect(id=3, enable=False, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9011]):
            return Guide(self.ctx)


class Guide(common.Trigger):
    def on_enter(self):
        self.debug_string(string='2번 영역에 들어가면 SetOnetimeEffect 트리거가 발동됩니다.')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9010]):
            return SetOnetimeEffectReady01(self.ctx)


class SetOnetimeEffectReady01(common.Trigger):
    def on_enter(self):
        self.debug_string(string='SetOnetimeEffect 2초 후에 시작됩니다.')
        self.set_onetime_effect(id=2, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SetOnetimeEffectReady02(self.ctx)


class SetOnetimeEffectReady02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SetOnetimeEffect01(self.ctx)


class SetOnetimeEffect01(common.Trigger):
    def on_enter(self):
        self.debug_string(string='SetOnetimeEffect 재생')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_black.xml')
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_black.xml')
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.debug_string(string='7초 후에 트리거가 리셋됩니다. 2번 영역 밖으로 나가세요.')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return Wait(self.ctx)


initial_state = Wait
