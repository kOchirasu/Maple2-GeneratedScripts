""" trigger/99999949/03_setonetimeeffect.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        self.set_onetime_effect(id=2, enable=False, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/Eff_co_targetBox_test_99999949_01.xml') # 툴벤치 상 좌표 : 	-600, -600, 1200

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9021]):
            return Guide(self.ctx)


class Guide(trigger_api.Trigger):
    def on_enter(self):
        self.debug_string(string='3번 영역에 들어가면 SetOnetime트리거가 발동됩니다.Effect targetBox 이펙트 테스트.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9020]):
            return SetOnetimeEffectReady01(self.ctx)


class SetOnetimeEffectReady01(trigger_api.Trigger):
    def on_enter(self):
        self.debug_string(string='SetOnetimeEffect 1초 후에 시작됩니다.')
        self.set_onetime_effect(id=1, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SetOnetimeEffect01(self.ctx)


class SetOnetimeEffect01(trigger_api.Trigger):
    def on_enter(self):
        self.debug_string(string='SetOnetimeEffect 재생')
        self.set_onetime_effect(id=2, enable=True, path='UGC_Test/Eff_Tutorial_Sound_target.xml')
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/Eff_co_targetBox_test_99999949_01.xml')
        self.set_time_scale(enable=True, startScale=1, endScale=0.2, duration=2, interpolator=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=True, startScale=0.2, endScale=1, duration=2, interpolator=2)
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/Eff_co_targetBox_test_99999949_01.xml')
        # action name="SetTimeScale" enable="1" endScale="1" duration="8" interpolator="2" /
        self.debug_string(string='5초 후에 트리거가 리셋됩니다. 3번 영역 밖으로 나가세요.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait(self.ctx)


initial_state = Wait
