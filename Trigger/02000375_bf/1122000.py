""" trigger/02000375_bf/1122000.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=13500, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ChangeBGM', value=1):
            return BGM변경(self.ctx)


class BGM변경(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=13500, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
