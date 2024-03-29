""" trigger/02000432_bf/buff_1.xml """
import trigger_api


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[2001]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[2001], skillId=40501001, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 사망(self.ctx)


class 사망(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 사망_버프제거(self.ctx)


class 사망_버프제거(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[2002], skillId=40501005, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return None


initial_state = 전투시작
