""" trigger/52000185_qd/main.xml """
import common


class Idle(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[2001], skillId=99910280, level=1, isPlayer=False, isSkillSet=True) # 벨라 변신
        self.add_buff(boxIds=[2001], skillId=99910280, level=1, isPlayer=False, isSkillSet=False) # 벨라 변신

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[2001], skillId=99910280, level=1, isPlayer=False, isSkillSet=True) # 벨라 변신
        self.add_buff(boxIds=[2001], skillId=99910280, level=1, isPlayer=False, isSkillSet=False) # 벨라 변신

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Idle(self.ctx)


initial_state = Idle
