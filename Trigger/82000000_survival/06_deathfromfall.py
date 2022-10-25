""" trigger/82000000_survival/06_deathfromfall.xml """
import common


class Setting(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return WaitSomeoneFall(self.ctx)


class WaitSomeoneFall(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9100]):
            return KillSomeoneFall(self.ctx)


class KillSomeoneFall(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9100], skillId=70001061, level=1, isPlayer=False, isSkillSet=False) # 추락사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return KillSomeoneFall(self.ctx)
        if not self.user_detected(boxIds=[9100]):
            return WaitSomeoneFall(self.ctx)


initial_state = Setting
