""" trigger/52010028_qd/view.xml """
import common


class 진동설정(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=301, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=401, enable=False, path='BG/sound/Eff_ShakeLand_01.xml')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2003]):
            return 흔들흔들(self.ctx)
        if self.user_detected(boxIds=[2006]):
            return 흔들흔들(self.ctx)
        if self.user_detected(boxIds=[2007]):
            return 흔들흔들(self.ctx)


class 흔들흔들(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=301, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=401, enable=True, path='BG/sound/Eff_ShakeLand_01.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 진동설정(self.ctx)


initial_state = 진동설정
