""" trigger/02020111_bf/skillbreakmission2.xml """
from common import *
import state


class 대기1(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=111, additionalEffectId=62100016, level=1):
            return 던전미션_체크1()


class 던전미션_체크1(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=101, additionalEffectId=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공1()


class 던전미션_스킬브레이크저지_성공1(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23039005)

    def on_tick(self) -> state.State:
        if not check_npc_additional_effect(spawnId=101, additionalEffectId=62100016, level=1):
            return 대기2()


class 대기2(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=151, additionalEffectId=62100016, level=1):
            return 던전미션_체크2()


class 던전미션_체크2(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=101, additionalEffectId=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공2()


class 던전미션_스킬브레이크저지_성공2(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23039005)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


