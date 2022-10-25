""" trigger/02020111_bf/skillbreakmission2.xml """
import common


class 대기1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_additional_effect(spawnId=111, additionalEffectId=62100016, level=1):
            return 던전미션_체크1(self.ctx)


class 던전미션_체크1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공1(self.ctx)


class 던전미션_스킬브레이크저지_성공1(common.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=23039005)

    def on_tick(self) -> common.Trigger:
        if not self.check_npc_additional_effect(spawnId=101, additionalEffectId=62100016, level=1):
            return 대기2(self.ctx)


class 대기2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_additional_effect(spawnId=151, additionalEffectId=62100016, level=1):
            return 던전미션_체크2(self.ctx)


class 던전미션_체크2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공2(self.ctx)


class 던전미션_스킬브레이크저지_성공2(common.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=23039005)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기1
