""" trigger/02100009_bf/buff_1.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 버프(self.ctx)


class 버프(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=50000205, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 대기(self.ctx)


initial_state = 대기
