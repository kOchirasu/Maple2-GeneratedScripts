""" trigger/02000207_bf/arm01.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ZakumArmDeath01', value=1):
            return 트로피지급(self.ctx)


class 트로피지급(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='ZakumArmDeath01')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
