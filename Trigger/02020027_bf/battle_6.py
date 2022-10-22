""" trigger/02020027_bf/battle_6.xml """
from common import *
import state


class 전투시작(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990009, key='summon_2', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1003]):
            return 스킬사용()


class 스킬사용(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='summon_2', value=1):
            return 몬스터소환()


class 몬스터소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=False, arg3=1000)

    def on_tick(self) -> state.State:
        if true():
            return None # Missing State: 길막삭제


