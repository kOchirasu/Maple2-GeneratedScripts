""" trigger/51000003_dg/buff.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Tutorial', value=1):
            return Tutorial_buff(self.ctx)


class Tutorial_buff(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Tutorial', value=0):
            return idle(self.ctx)
        if self.user_detected(boxIds=[701]):
            return buff(self.ctx)


class buff(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000085, level=1, isSkillSet=False) # 무적

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Tutorial', value=0):
            return idle(self.ctx)
        if self.true():
            return Tutorial_buff(self.ctx)


initial_state = idle
