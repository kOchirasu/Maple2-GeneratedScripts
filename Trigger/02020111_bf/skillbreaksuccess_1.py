""" trigger/02020111_bf/skillbreaksuccess_1.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakSuccess_1', value=1) and self.user_value(key='SkillBreakSuccess_2', value=1) and self.user_value(key='SkillBreakSuccess_3', value=1) and self.user_value(key='SkillBreakSuccess_4', value=1):
            return 버프발동(self.ctx)


class 버프발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[101], skillId=62100027, level=1, isPlayer=True)
        self.add_buff(boxIds=[1001], skillId=75000002, level=1)
        self.add_buff(boxIds=[1002], skillId=75000002, level=1)
        self.add_buff(boxIds=[1003], skillId=75000002, level=1)
        self.add_buff(boxIds=[1004], skillId=75000002, level=1)
        self.add_buff(boxIds=[1005], skillId=75000002, level=1)
        self.set_ambient_light(primary=[183,189,201])
        self.set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])
        self.add_buff(boxIds=[101], skillId=70002171, level=1, isPlayer=True, isSkillSet=False)
        self.add_buff(boxIds=[101], skillId=62100026, level=1, isPlayer=True, isSkillSet=False)
        self.set_user_value(triggerId=900103, key='Lapenta_Attack_Guide', value=2)
        self.set_user_value(triggerId=900204, key='Message', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakSuccess_1', value=0) and self.user_value(key='SkillBreakSuccess_2', value=0) and self.user_value(key='SkillBreakSuccess_3', value=0) and self.user_value(key='SkillBreakSuccess_4', value=0) and self.user_value(key='SkillBreakSuccess_Reset', value=0):
            return 시작(self.ctx)


initial_state = 시작
