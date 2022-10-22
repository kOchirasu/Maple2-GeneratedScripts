""" trigger/02020101_bf/skillbreakmission2.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=101, additionalEffectId=62100024, level=1):
            return 던전미션_체크()


class 던전미션_체크(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=101, additionalEffectId=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공()


class 던전미션_스킬브레이크저지_성공(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23038005)

    def on_tick(self) -> state.State:
        if not check_npc_additional_effect(spawnId=101, additionalEffectId=62100024, level=1):
            return 대기()


