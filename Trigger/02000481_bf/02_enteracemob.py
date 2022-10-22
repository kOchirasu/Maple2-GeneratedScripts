""" trigger/02000481_bf/02_enteracemob.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[900,901]) # Mob_Enter
        set_user_value(key='MobSpawn', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='MobSpawn', value=1):
            return MobSpawn01()


class MobSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[900], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return MobSpawn02()


class MobSpawn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[901], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900,901]):
            return Reset()


class Reset(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return MobSpawn01()


