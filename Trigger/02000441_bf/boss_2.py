""" trigger/02000441_bf/boss_2.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='monster_respawn', value=1):
            return 몬스터체력_75()


class 몬스터체력_75(state.State):
    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=75, spawnId=209, isRelative=True):
            return 몬스터체력_35()

    def on_exit(self):
        create_monster(spawnIds=[210,211,212,213], arg2=True)


class 몬스터체력_35(state.State):
    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=35, spawnId=209, isRelative=True):
            return 몬스터_마지막_리스폰()


class 몬스터_마지막_리스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[214,215,216,217], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return None


