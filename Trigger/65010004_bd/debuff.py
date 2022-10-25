""" trigger/65010004_bd/debuff.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 디버프(self.ctx)


class 디버프(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=70000040, level=1, isPlayer=False, isSkillSet=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)


initial_state = 대기
