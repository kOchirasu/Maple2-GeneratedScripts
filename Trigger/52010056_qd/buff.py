""" trigger/52010056_qd/buff.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[3]):
            return Buff_B(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[2]):
            return Buff_B(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[91000054], questStates=[1]):
            return Buff_B(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[91000053], questStates=[3]):
            return Buff_A(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[91000053], questStates=[2]):
            return Buff_A(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[91000053], questStates=[1]):
            return Buff_A(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[91000052], questStates=[3]):
            return Buff_A(self.ctx)


class Buff_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[2001], skillId=99910300, level=1, isPlayer=False, isSkillSet=True) # 트리스탄 변신
        self.add_buff(boxIds=[2001], skillId=99910300, level=1, isPlayer=False, isSkillSet=False) # 트리스탄 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Ready(self.ctx)


class Buff_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[2001], skillId=99910330, level=1, isPlayer=False, isSkillSet=True) # 트리스탄 변신
        self.add_buff(boxIds=[2001], skillId=99910330, level=1, isPlayer=False, isSkillSet=False) # 트리스탄 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Ready(self.ctx)


initial_state = Idle
