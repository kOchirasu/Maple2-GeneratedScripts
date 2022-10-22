""" trigger/99999949/03_setonetimeeffect.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        set_onetime_effect(id=2, enable=False, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/Eff_co_targetBox_test_99999949_01.xml') # 툴벤치 상 좌표 : 	-600, -600, 1200

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9021]):
            return Guide()


class Guide(state.State):
    def on_enter(self):
        debug_string(string='3번 영역에 들어가면 SetOnetime트리거가 발동됩니다.Effect targetBox 이펙트 테스트.')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9020]):
            return SetOnetimeEffectReady01()


class SetOnetimeEffectReady01(state.State):
    def on_enter(self):
        debug_string(string='SetOnetimeEffect 1초 후에 시작됩니다.')
        set_onetime_effect(id=1, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SetOnetimeEffect01()


class SetOnetimeEffect01(state.State):
    def on_enter(self):
        debug_string(string='SetOnetimeEffect 재생')
        set_onetime_effect(id=2, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        set_onetime_effect(id=3, enable=True, path='BG/Common/Eff_co_targetBox_test_99999949_01.xml')
        set_time_scale(enable=True, startScale=1, endScale=0.2, duration=2, interpolator=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=0.2, endScale=1, duration=2, interpolator=2)
        set_onetime_effect(id=3, enable=False, path='BG/Common/Eff_co_targetBox_test_99999949_01.xml') # action name="SetTimeScale" enable="1" endScale="1" duration="8" interpolator="2" /
        debug_string(string='5초 후에 트리거가 리셋됩니다. 3번 영역 밖으로 나가세요.')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait()


