""" trigger/82000002_survival/13_relicmob_green.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1300,1301,1302,1303,1304,1305,1306,1307,1308,1309])
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
        create_monster(spawnIds=[1300], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1300]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1301], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1301]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1302], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1302]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1303], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1303]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1304], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1304]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1305], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1305]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1306], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1306]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1307], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1307]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn09(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1308], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1308]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class MobSpawn10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1309], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1309]):
            return Notice()
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class Notice(state.State):
    def on_enter(self):
        set_user_value(triggerId=16, key='RelicMobGreenDie', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRemove', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1300,1301,1302,1303,1304,1305,1306,1307,1308,1309])


