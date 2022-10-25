""" trigger/02000471_bf/buff.xml """
import common


# 에디셔널 이펙트를 계속 걸어줌
class idle(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[720], skillId=71000009, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return buff_01(self.ctx)


class buff_01(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[720], skillId=71000009, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


initial_state = idle
