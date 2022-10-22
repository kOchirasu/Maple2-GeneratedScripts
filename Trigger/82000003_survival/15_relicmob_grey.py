""" trigger/82000003_survival/15_relicmob_grey.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1500,1501,1502,1503,1504,1505,1506,1507,1508,1509])
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
        create_monster(spawnIds=[1500], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1500]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1501], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1501]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1502], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1502]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1503], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1503]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1504], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1504]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1505], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1505]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1506], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1506]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1507], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1507]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn09(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1508]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1509], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1509]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class Notice(state.State):
    def on_enter(self):
        set_user_value(triggerId=16, key='RelicMobGreyDie', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1500,1501,1502,1503,1504,1505,1506,1507,1508,1509])


