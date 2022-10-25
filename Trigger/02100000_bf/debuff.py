""" trigger/02100000_bf/debuff.xml """
import common


class 유저감지(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[106]):
            return 버프(self.ctx)


class 버프(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=70000130, level=1, isPlayer=False, isSkillSet=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버프_2(self.ctx)


class 버프_2(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=70000130, level=1, isPlayer=False, isSkillSet=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버프_3(self.ctx)


class 버프_3(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=70000130, level=1, isPlayer=False, isSkillSet=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버프_4(self.ctx)


class 버프_4(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=70000130, level=1, isPlayer=False, isSkillSet=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버프_5(self.ctx)


class 버프_5(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=70000131, level=1, isPlayer=False, isSkillSet=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return 버프(self.ctx)


initial_state = 유저감지
