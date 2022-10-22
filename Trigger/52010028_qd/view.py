""" trigger/52010028_qd/view.xml """
from common import *
import state


class 진동설정(state.State):
    def on_enter(self):
        set_onetime_effect(id=301, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=401, enable=False, path='BG/sound/Eff_ShakeLand_01.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2003]):
            return 흔들흔들()
        if user_detected(boxIds=[2006]):
            return 흔들흔들()
        if user_detected(boxIds=[2007]):
            return 흔들흔들()


class 흔들흔들(state.State):
    def on_enter(self):
        set_onetime_effect(id=301, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=401, enable=True, path='BG/sound/Eff_ShakeLand_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 진동설정()


