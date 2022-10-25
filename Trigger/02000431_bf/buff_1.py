""" trigger/02000431_bf/buff_1.xml """
import common


class 전투시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[2199]):
            return 버프(self.ctx)


class 버프(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[2199], skillId=40501006, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return None


initial_state = 전투시작
