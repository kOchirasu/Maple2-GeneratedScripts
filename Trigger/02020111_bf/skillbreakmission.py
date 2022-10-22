""" trigger/02020111_bf/skillbreakmission.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakMissionReset', value=1):
            return 대기_1차_발동체크()


class 대기_1차_발동체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakMissionReset', value=0):
            return 대기()
        if check_npc_additional_effect(spawnId=111, additionalEffectId=62100016, level=1):
            return 던전미션1차_체크()


class 던전미션1차_체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakMissionReset', value=0):
            return 대기()
        if all_of():
            return 던전미션1차_스킬브레이크저지_성공()
        if check_npc_additional_effect(spawnId=101, additionalEffectId=70002181, level=1):
            return 던전미션1차_스킬브레이크저지_실패()


class 던전미션1차_스킬브레이크저지_성공(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23039004)

    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakMissionReset', value=0):
            return 대기()
        if wait_tick(waitTick=1000):
            return 대기_2차()


class 던전미션1차_스킬브레이크저지_실패(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakMissionReset', value=0):
            return 대기()
        if wait_tick(waitTick=1000):
            return 대기_2차()


class 대기_2차(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakMissionReset', value=0):
            return 대기()
        if check_npc_additional_effect(spawnId=115, additionalEffectId=62100016, level=1):
            return 던전미션2차_체크()


class 던전미션2차_체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakMissionReset', value=0):
            return 대기()
        if all_of():
            return 던전미션2차_스킬브레이크저지_성공()
        if check_npc_additional_effect(spawnId=101, additionalEffectId=70002181, level=1):
            return 던전미션2차_스킬브레이크저지_실패()


class 던전미션2차_스킬브레이크저지_성공(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23039004)

    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakMissionReset', value=0):
            return 대기()
        if wait_tick(waitTick=1000):
            return 종료()


class 던전미션2차_스킬브레이크저지_실패(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakMissionReset', value=0):
            return 대기()
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


