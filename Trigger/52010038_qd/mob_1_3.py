""" trigger/52010038_qd/mob_1_3.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='bombStart', value=1):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2097], arg2=False)
        spawn_npc_range(rangeIds=[2008,2009,2010], isAutoTargeting=True)
        spawn_npc_range(rangeIds=[2101,2102,2103,2104,2105,2106,2107], isAutoTargeting=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2097]):
            set_user_value(triggerId=999001, key='CoreIsDead', value=1)
            return 종료()


class 종료(state.State):
    pass


