""" trigger/52000185_qd/main.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[2001], skillId=99910280, level=1, isPlayer=False, isSkillSet=True) # 벨라 변신
        self.add_buff(boxIds=[2001], skillId=99910280, level=1, isPlayer=False, isSkillSet=False) # 벨라 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[2001], skillId=99910280, level=1, isPlayer=False, isSkillSet=True) # 벨라 변신
        self.add_buff(boxIds=[2001], skillId=99910280, level=1, isPlayer=False, isSkillSet=False) # 벨라 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Idle(self.ctx)


initial_state = Idle
