""" trigger/52000084_qd/buff.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=70000115)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return 버프(self.ctx)


class 버프(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[199], skillId=70000115, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버프(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
