""" trigger/02000311_bf/buff_01.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Buff_01', value=1):
            return Buff_Ready(self.ctx)


class Buff_Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return Buff_01(self.ctx)


class Buff_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return Buff_01_Start(self.ctx)


class Buff_01_Start(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=50003006, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Buff_01(self.ctx)


initial_state = idle
