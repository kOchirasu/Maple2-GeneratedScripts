""" trigger/02000443_bf/error.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return buff_1(self.ctx)


class buff_1(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=49200002, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=60000):
            return buff_2(self.ctx)
        if self.user_value(key='debuff', value=1):
            return None # Missing State: 끝


class buff_2(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=49200002, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=60000):
            return buff_1(self.ctx)


initial_state = 시작
