""" trigger/65010006_bd/debuff.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 체크(self.ctx)


class 체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            return 디버프(self.ctx)


class 디버프(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[102], skillId=70000040, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 체크(self.ctx)


initial_state = 시작대기중
