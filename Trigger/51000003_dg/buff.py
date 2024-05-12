""" trigger/51000003_dg/buff.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Tutorial', value=1):
            return Tutorial_buff(self.ctx)


class Tutorial_buff(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Tutorial', value=0):
            return idle(self.ctx)
        if self.user_detected(boxIds=[701]):
            return buff(self.ctx)


class buff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[701], skillId=70000085, level=1, isSkillSet=False) # 무적

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Tutorial', value=0):
            return idle(self.ctx)
        if self.true():
            return Tutorial_buff(self.ctx)


initial_state = idle
