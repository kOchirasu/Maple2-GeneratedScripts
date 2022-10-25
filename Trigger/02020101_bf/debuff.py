""" trigger/02020101_bf/debuff.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Debuff', value=1):
            return 디버프시작(self.ctx)
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)


class 디버프시작(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900002, key='Debuff', value=0)
        self.add_buff(boxIds=[1004], skillId=70002122, level=1, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Debuff', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900002, key='Debuff', value=0)
        self.remove_buff(boxId=1004, skillId=70002122, isPlayer=True)
        self.add_buff(boxIds=[1004], skillId=70002123, level=1, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Debuff', value=0):
            return 대기(self.ctx)


initial_state = 대기
