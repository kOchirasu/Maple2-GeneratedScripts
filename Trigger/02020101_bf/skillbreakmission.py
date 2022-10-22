""" trigger/02020101_bf/skillbreakmission.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=101, additionalEffectId=62100024, level=1):
            return 던전미션_체크()


class 던전미션_체크(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 던전미션_스킬브레이크저지_성공()
        if check_npc_additional_effect(spawnId=101, additionalEffectId=70002181, level=1):
            return 던전미션_스킬브레이크저지_실패()


class 던전미션_스킬브레이크저지_성공(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23038004)

    def on_tick(self) -> state.State:
        if not check_npc_additional_effect(spawnId=101, additionalEffectId=62100024, level=1):
            return 대기()


class 던전미션_스킬브레이크저지_실패(state.State):
    def on_tick(self) -> state.State:
        if not check_npc_additional_effect(spawnId=101, additionalEffectId=62100024, level=1):
            return 대기()


class 종료(state.State):
    pass


