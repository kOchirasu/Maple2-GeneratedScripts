""" trigger/02020101_bf/skillbreak.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900001, key='SkillBreakFail', value=0)

    def on_tick(self) -> common.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002181, level=1):
            return 스킬브레이크_실패(self.ctx)


class 스킬브레이크_실패(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[1003], skillId=70002151, level=1, isSkillSet=False)
        self.set_user_value(triggerId=900001, key='SkillBreakFail', value=1)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
