""" trigger/02020111_bf/light_on.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 대기(self.ctx)
        if self.all_of():
            return 시작(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라이트_변경(self.ctx)


class 라이트_변경(trigger_api.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[183,189,201])
        self.set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])

    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 시작(self.ctx)


initial_state = 시작
