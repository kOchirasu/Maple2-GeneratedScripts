""" trigger/02000483_bf/05_hallwaymobwave.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[930,931,932,933]) # Mob
        set_user_value(key='MobWave', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='MobWave', value=1):
            return MobSpawn01()


class MobSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[930], arg2=False) # Mob

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return MobSpawn02()


class MobSpawn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[931], arg2=False) # Mob

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return MobSpawn03()


class MobSpawn03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[932], arg2=False) # Mob

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return MobSpawn04()


class MobSpawn04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[933], arg2=False) # Mob


