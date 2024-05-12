""" trigger/02020111_bf/skillbreakmission.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset', value=1):
            return 대기_1차_발동체크(self.ctx)


class 대기_1차_발동체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset', value=0):
            return 대기(self.ctx)
        if self.check_npc_additional_effect(spawnId=111, additionalEffectId=62100016, level=1):
            # <블루라펜샤드 1차 스킬 브레이크 체크>
            return 던전미션1차_체크(self.ctx)


class 던전미션1차_체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset', value=0):
            return 대기(self.ctx)
        # all_of:  <쉴드가 깨지기까지 8초보다 많은 시간이 남은 경우 = 6초 이내로 파괴>
        # all_of:  <스킬 브레이크 성공 애디셔널>
        if self.check_npc_extra_data(spawnPointID='111', extraDataKey='brokenShieldRemainTick', extraDataValue='8000', operator='GreaterEqual') and self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002171, level=1):
            return 던전미션1차_스킬브레이크저지_성공(self.ctx)
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002181, level=1):
            # <스킬 브레이크 실패 애디셔널>
            return 던전미션1차_스킬브레이크저지_실패(self.ctx)


class 던전미션1차_스킬브레이크저지_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(missionId=23039004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 대기_2차(self.ctx)


class 던전미션1차_스킬브레이크저지_실패(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 대기_2차(self.ctx)


class 대기_2차(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset', value=0):
            return 대기(self.ctx)
        if self.check_npc_additional_effect(spawnId=115, additionalEffectId=62100016, level=1):
            # <블루라펜샤드 2차 스킬 브레이크 체크>
            return 던전미션2차_체크(self.ctx)


class 던전미션2차_체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset', value=0):
            return 대기(self.ctx)
        # all_of:  <쉴드가 깨지기까지 8초보다 많은 시간이 남은 경우 = 6초 이내로 파괴>
        # all_of:  <스킬 브레이크 성공 애디셔널>
        if self.check_npc_extra_data(spawnPointID='115', extraDataKey='brokenShieldRemainTick', extraDataValue='8000', operator='GreaterEqual') and self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002171, level=1):
            return 던전미션2차_스킬브레이크저지_성공(self.ctx)
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002181, level=1):
            # <스킬 브레이크 실패 애디셔널>
            return 던전미션2차_스킬브레이크저지_실패(self.ctx)


class 던전미션2차_스킬브레이크저지_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(missionId=23039004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 던전미션2차_스킬브레이크저지_실패(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
