""" trigger/02000207_bf/arm05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ZakumArmDeath05', value=1):
            return 트로피지급(self.ctx)


class 트로피지급(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='ZakumArmDeath05')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
