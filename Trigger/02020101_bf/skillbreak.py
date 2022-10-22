""" trigger/02020101_bf/skillbreak.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=900001, key='SkillBreakFail', value=0)

    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=101, additionalEffectId=70002181, level=1):
            return 스킬브레이크_실패()


class 스킬브레이크_실패(state.State):
    def on_enter(self):
        add_buff(boxIds=[1003], skillId=70002151, level=1, arg5=False)
        set_user_value(triggerId=900001, key='SkillBreakFail', value=1)

    def on_tick(self) -> state.State:
        if true():
            return 대기()


class 종료(state.State):
    pass


