""" trigger/82000002_survival/11_relicmob_red.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109])
        set_user_value(key='RelicMobSpawn', value=0)
        set_user_value(key='RelicMobRemove', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RelicMobSpawn', value=1):
            return Delay()


class Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return MobSpawnRandom()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawnRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return MobSpawn01()
        if random_condition(rate=10):
            return MobSpawn02()
        if random_condition(rate=10):
            return MobSpawn03()
        if random_condition(rate=10):
            return MobSpawn04()
        if random_condition(rate=10):
            return MobSpawn05()
        if random_condition(rate=10):
            return MobSpawn06()
        if random_condition(rate=10):
            return MobSpawn07()
        if random_condition(rate=10):
            return MobSpawn08()
        if random_condition(rate=10):
            return MobSpawn09()
        if random_condition(rate=10):
            return MobSpawn10()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()


class MobSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1100], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1100]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1101], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1101]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1102], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1102]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1103], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1103]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1104], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1104]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1105], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1105]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1106], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1106]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1107], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1107]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn09(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1108], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1108]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1109], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1109]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class Notice(state.State):
    def on_enter(self):
        set_user_value(triggerId=16, key='RelicMobRedDie', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109])


