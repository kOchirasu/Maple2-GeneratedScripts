""" trigger/99999907/12000013.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000013], state=2)

    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=50):
            return 반응대기(self.ctx)
        if self.random_condition(rate=50):
            return 종료(self.ctx)


class 반응대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000013], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000013], stateValue=0):
            return 랜덤버프(self.ctx)


class 랜덤버프(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            self.add_buff(boxIds=[199], skillId=70000008, level=1, isPlayer=False, isSkillSet=False)
            return 종료(self.ctx)
        if self.random_condition(rate=30):
            self.add_buff(boxIds=[199], skillId=70000008, level=1, isPlayer=False, isSkillSet=False)
            return 종료(self.ctx)
        if self.random_condition(rate=40):
            self.add_buff(boxIds=[199], skillId=70000008, level=1, isPlayer=False, isSkillSet=False)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
