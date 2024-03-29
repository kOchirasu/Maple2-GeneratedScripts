""" trigger/02020111_bf/skillbreakmission2.xml """
import trigger_api


class 대기1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawnId=111, additionalEffectId=62100016, level=1):
            return 던전미션_체크1(self.ctx)


class 던전미션_체크1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공1(self.ctx)


class 던전미션_스킬브레이크저지_성공1(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=23039005)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_npc_additional_effect(spawnId=101, additionalEffectId=62100016, level=1):
            return 대기2(self.ctx)


class 대기2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawnId=151, additionalEffectId=62100016, level=1):
            return 던전미션_체크2(self.ctx)


class 던전미션_체크2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공2(self.ctx)


class 던전미션_스킬브레이크저지_성공2(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=23039005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기1
