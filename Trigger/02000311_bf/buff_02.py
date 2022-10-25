""" trigger/02000311_bf/buff_02.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Buff_02', value=1):
            return Buff_02_Ready(self.ctx)


class Buff_02_Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[702]):
            return Buff_02(self.ctx)


class Buff_02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[702]):
            return Buff_02_Start(self.ctx)


class Buff_02_Start(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[702], skillId=50003006, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Buff_02(self.ctx)


initial_state = idle
