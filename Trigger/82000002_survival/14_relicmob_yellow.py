""" trigger/82000002_survival/14_relicmob_yellow.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1400,1401,1402,1403,1404,1405,1406,1407,1408,1409])
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
        create_monster(spawnIds=[1400], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1400]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1401], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1401]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1402], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1402]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1403], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1403]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1404], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1404]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1405], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1405]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1406], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1406]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1407], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1407]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn09(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1408], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1408]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1409], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1409]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class Notice(state.State):
    def on_enter(self):
        set_user_value(triggerId=16, key='RelicMobYellowDie', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1400,1401,1402,1403,1404,1405,1406,1407,1408,1409])


