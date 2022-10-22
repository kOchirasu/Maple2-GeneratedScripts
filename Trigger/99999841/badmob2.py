""" trigger/99999841/badmob2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990004, key='BadMob', value=0)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='902', value=1):
            return 몬스터스폰()


class 몬스터스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[992], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[991,992,993]):
            return 신호쏴주기()


class 신호쏴주기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990004, key='BadMob', value=1)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    def on_tick(self) -> state.State:
        if dungeon_variable(varID='902', value=0):
            return 대기()


