""" trigger/02020111_bf/skillbreaksuccess_2.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakSuccess_5') >= 1 and self.user_value(key='SkillBreakSuccess_6') >= 1 and self.user_value(key='SkillBreakSuccess_7') >= 1 and self.user_value(key='SkillBreakSuccess_8') >= 1:
            return 버프발동(self.ctx)


class 버프발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[101], skill_id=62100027, level=1, is_player=True)
        self.add_buff(box_ids=[1001], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1002], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1003], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1004], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1005], skill_id=75000002, level=1)
        self.set_ambient_light(primary=[183,189,201])
        self.set_directional_light(diffuse_color=[192,210,211], specular_color=[170,170,170])
        self.add_buff(box_ids=[101], skill_id=70002171, level=1, is_player=True, is_skill_set=False)
        self.add_buff(box_ids=[101], skill_id=62100026, level=1, is_player=True, is_skill_set=False)
        self.set_user_value(trigger_id=900103, key='Lapenta_Attack_Guide', value=2)
        self.set_user_value(trigger_id=900204, key='Message', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakSuccess_5') >= 0 and self.user_value(key='SkillBreakSuccess_6') >= 0 and self.user_value(key='SkillBreakSuccess_7') >= 0 and self.user_value(key='SkillBreakSuccess_8') >= 0 and self.user_value(key='SkillBreakSuccess_Reset') >= 0:
            return 시작(self.ctx)


initial_state = 시작
