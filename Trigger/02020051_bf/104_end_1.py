""" trigger/02020051_bf/104_end_1.xml """
from common import *
import state


class 사망조건(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='End', value=1):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        set_user_value(triggerId=103, key='Main', value=2)
        set_user_value(triggerId=107, key='Text', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 준비_2()


class 준비_2(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', script='$02020051_BF__104_END_1__0$', duration=5684, voice='ko/Npc/00002201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 몬스터사망_1()


class 몬스터사망_1(state.State):
    def on_tick(self) -> state.State:
        if any_one():
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=102, key='Timmer', value=3)
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료_2()


class 종료_2(state.State):
    def on_enter(self):
        set_user_value(triggerId=103, key='Main', value=2)
        set_user_value(triggerId=102, key='Timmer', value=2)
        set_user_value(triggerId=102, key='Timmer', value=3)
        set_user_value(triggerId=101, key='Potion', value=2)
        set_user_value(triggerId=105, key='Summon_monster', value=2)
        set_user_value(triggerId=106, key='Summon_monster_2', value=2)
        set_user_value(triggerId=107, key='Text', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='End', value=2):
            return 사망조건()


