""" trigger/52000063_qd/random_skill_c.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[607], visible=False)
        self.set_effect(triggerIds=[608], visible=False)
        self.set_effect(triggerIds=[609], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='gameStart', value=1):
            return 감지대기(self.ctx)


class 감지대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[607], visible=True)
        self.set_effect(triggerIds=[608], visible=True)
        self.set_effect(triggerIds=[609], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[113]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[607], visible=False)
        self.set_effect(triggerIds=[608], visible=False)
        self.set_effect(triggerIds=[609], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=80):
            self.add_buff(boxIds=[199], skillId=70000008, level=1, isPlayer=False, isSkillSet=False)
            return 종료(self.ctx)
        if self.random_condition(rate=20):
            self.add_buff(boxIds=[199], skillId=70000009, level=1, isPlayer=False, isSkillSet=False)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
