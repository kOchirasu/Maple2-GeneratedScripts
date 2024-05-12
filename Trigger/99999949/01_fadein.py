""" trigger/99999949/01_fadein.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=False) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return Guide(self.ctx)


class Guide(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(string='1번 영역에 들어가면 화면 페이드인 트리거가 시작됩니다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(string='fadein')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[5000], visible=True) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12000):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(string='fadeout')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[5000], visible=False) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(string='3초 후에 트리거가 리셋됩니다. 1번 영역 밖으로 나가세요.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait(self.ctx)


initial_state = Wait
