""" trigger/02100009_bf/clear.xml """
import common


class 끝1(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1000049], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 끝2(self.ctx)


class 끝2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return 끝3(self.ctx)


class 끝3(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[100000002], skillId=50000217, level=1, isPlayer=True, isSkillSet=False)
        self.set_skill(triggerIds=[1000049], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return None


initial_state = 끝1
