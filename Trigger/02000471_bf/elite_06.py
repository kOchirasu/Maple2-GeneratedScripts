""" trigger/02000471_bf/elite_06.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return spawn(self.ctx)


class spawn(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Buff', value=1):
            return buff(self.ctx)


class buff(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[1999], skillId=70002051, level=1, isPlayer=True, isSkillSet=False)
        self.add_buff(boxIds=[306], skillId=70002051, level=1, isPlayer=True, isSkillSet=False)


initial_state = idle
