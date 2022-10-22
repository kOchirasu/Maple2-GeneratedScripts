""" trigger/82000003_survival/12_relicmob_skyblue.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209])
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
        create_monster(spawnIds=[1200], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1200]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1201], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1201]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1202], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1202]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1203], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1203]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1204], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1204]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1205], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1205]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1206], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1206]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1207], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1207]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn09(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1208], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1208]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1209], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1209]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class Notice(state.State):
    def on_enter(self):
        set_user_value(triggerId=16, key='RelicMobSkyblueDie', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209])


