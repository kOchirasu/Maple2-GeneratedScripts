""" trigger/02020101_bf/skillbreakmission.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=62100024, level=1):
            return 던전미션_체크(self.ctx)


class 던전미션_체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 던전미션_스킬브레이크저지_성공(self.ctx)
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002181, level=1):
            return 던전미션_스킬브레이크저지_실패(self.ctx)


class 던전미션_스킬브레이크저지_성공(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=23038004)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_npc_additional_effect(spawnId=101, additionalEffectId=62100024, level=1):
            return 대기(self.ctx)


class 던전미션_스킬브레이크저지_실패(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_npc_additional_effect(spawnId=101, additionalEffectId=62100024, level=1):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
