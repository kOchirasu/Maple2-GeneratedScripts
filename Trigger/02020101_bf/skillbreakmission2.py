""" trigger/02020101_bf/skillbreakmission2.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=62100024, level=1):
            return 던전미션_체크(self.ctx)


class 던전미션_체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공(self.ctx)


class 던전미션_스킬브레이크저지_성공(common.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=23038005)

    def on_tick(self) -> common.Trigger:
        if not self.check_npc_additional_effect(spawnId=101, additionalEffectId=62100024, level=1):
            return 대기(self.ctx)


initial_state = 대기
