""" trigger/02000486_bf/104_clear.xml """
import common


class 끝1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9901]):
            return 끝2(self.ctx)


class 끝2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return 끝3(self.ctx)


class 끝3(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[900], skillId=50002505, level=1, isPlayer=True, isSkillSet=False)
        self.add_buff(boxIds=[901], skillId=50002505, level=1, isPlayer=True, isSkillSet=False)
        self.set_skill(triggerIds=[1000049], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return None


initial_state = 끝1
