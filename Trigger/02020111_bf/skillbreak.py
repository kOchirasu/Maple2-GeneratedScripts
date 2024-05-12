""" trigger/02020111_bf/skillbreak.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=900001, key='SkillBreakFail', value=0)
        self.set_user_value(triggerId=900008, key='SkillBreakFail', value=3)
        self.set_user_value(triggerId=900009, key='SkillBreakFail', value=3)
        self.set_user_value(triggerId=900010, key='SkillBreakFail', value=3)
        self.set_user_value(triggerId=900011, key='SkillBreakFail', value=3)
        self.set_user_value(triggerId=900002, key='Summon', value=2)
        self.set_user_value(triggerId=900007, key='Summon', value=2)
        self.set_user_value(triggerId=900003, key='Summon_Enemy_1', value=2)
        self.set_user_value(triggerId=900005, key='Lapenta_Attack', value=2)
        self.set_user_value(triggerId=900006, key='Lapenta_Attack_2', value=2)
        self.set_user_value(triggerId=900102, key='Phase', value=3)
        self.set_user_value(triggerId=900004, key='Movement', value=2)
        self.set_user_value(triggerId=900201, key='Movement', value=2)
        self.set_user_value(triggerId=900202, key='Movement', value=2)
        self.set_user_value(triggerId=900203, key='Movement', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002181, level=1):
            return 스킬브레이크_실패(self.ctx)


class 스킬브레이크_실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[101], skillId=62100026, level=1, isPlayer=True)
        self.add_buff(boxIds=[101], skillId=70002185, level=1, isPlayer=True) # 스킬브레이크 체크를 제거한다.
        self.set_ambient_light(primary=[183,189,201])
        self.set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])
        self.add_buff(boxIds=[1006], skillId=70002151, level=1, isSkillSet=False)
        self.set_user_value(triggerId=900001, key='SkillBreakFail', value=1)
        # self.set_user_value(triggerId=900002, key='SkillBreakFail', value=1)
        # self.set_user_value(triggerId=900003, key='SkillBreakFail', value=1)
        self.set_user_value(triggerId=900008, key='SkillBreakFail', value=1)
        self.set_user_value(triggerId=900009, key='SkillBreakFail', value=1)
        self.set_user_value(triggerId=900010, key='SkillBreakFail', value=1)
        self.set_user_value(triggerId=900011, key='SkillBreakFail', value=1)
        self.set_user_value(triggerId=900002, key='Summon', value=0)
        self.set_user_value(triggerId=900007, key='Summon', value=0)
        self.set_user_value(triggerId=900003, key='Summon_Enemy_1', value=0)
        self.set_user_value(triggerId=900004, key='Movement', value=0)
        self.set_user_value(triggerId=900201, key='Movement', value=0)
        self.set_user_value(triggerId=900202, key='Movement', value=0)
        self.set_user_value(triggerId=900203, key='Movement', value=0)
        self.set_user_value(triggerId=900103, key='Lapenta_Attack_Guide', value=2)
        self.set_user_value(triggerId=900104, key='SkillBreakSuccess_Reset', value=0)
        self.set_user_value(triggerId=900104, key='SkillBreakSuccess_1', value=0)
        self.set_user_value(triggerId=900104, key='SkillBreakSuccess_2', value=0)
        self.set_user_value(triggerId=900104, key='SkillBreakSuccess_3', value=0)
        self.set_user_value(triggerId=900104, key='SkillBreakSuccess_4', value=0)
        self.set_user_value(triggerId=900105, key='SkillBreakSuccess_Reset', value=0)
        self.set_user_value(triggerId=900105, key='SkillBreakSuccess_5', value=0)
        self.set_user_value(triggerId=900105, key='SkillBreakSuccess_6', value=0)
        self.set_user_value(triggerId=900105, key='SkillBreakSuccess_7', value=0)
        self.set_user_value(triggerId=900105, key='SkillBreakSuccess_8', value=0)
        self.set_user_value(triggerId=900102, key='Phase', value=1)
        self.set_portal(portalId=5, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=7, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=8, visible=False, enable=False, minimapVisible=False)
        self.set_user_value(triggerId=900301, key='Light_On_1', value=1)
        self.set_user_value(triggerId=900301, key='Light_On_2', value=1)
        self.set_user_value(triggerId=900301, key='Light_On_3', value=1)
        self.set_user_value(triggerId=900301, key='Light_On_4', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 스킬브레이크_실패_2(self.ctx)


class 스킬브레이크_실패_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=900005, key='Lapenta_Attack', value=0)
        self.set_user_value(triggerId=900006, key='Lapenta_Attack_2', value=0)
        self.set_user_value(triggerId=900102, key='Phase', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
