""" trigger/02000471_bf/elite_02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return spawn(self.ctx)


class spawn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Buff', value=1):
            return buff(self.ctx)


class buff(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[1999], skillId=70002011, level=1, isPlayer=True, isSkillSet=False)
        self.add_buff(boxIds=[302], skillId=70002011, level=1, isPlayer=True, isSkillSet=False)


initial_state = idle
