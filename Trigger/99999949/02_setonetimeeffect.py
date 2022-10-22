""" trigger/99999949/02_setonetimeeffect.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_black.xml')
        set_onetime_effect(id=2, enable=False, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        set_onetime_effect(id=3, enable=False, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        set_onetime_effect(id=4, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9011]):
            return Guide()


class Guide(state.State):
    def on_enter(self):
        debug_string(string='2번 영역에 들어가면 SetOnetimeEffect 트리거가 발동됩니다.')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9010]):
            return SetOnetimeEffectReady01()


class SetOnetimeEffectReady01(state.State):
    def on_enter(self):
        debug_string(string='SetOnetimeEffect 2초 후에 시작됩니다.')
        set_onetime_effect(id=2, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SetOnetimeEffectReady02()


class SetOnetimeEffectReady02(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SetOnetimeEffect01()


class SetOnetimeEffect01(state.State):
    def on_enter(self):
        debug_string(string='SetOnetimeEffect 재생')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_black.xml')
        set_onetime_effect(id=4, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_black.xml')
        set_onetime_effect(id=4, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        debug_string(string='7초 후에 트리거가 리셋됩니다. 2번 영역 밖으로 나가세요.')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Wait()

