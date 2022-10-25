""" trigger/82000003_survival/12_relicmob_skyblue.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209])
        self.set_user_value(key='RelicMobSpawn', value=0)
        self.set_user_value(key='RelicMobRemove', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RelicMobSpawn', value=1):
            return Delay(self.ctx)


class Delay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return MobSpawnRandom(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawnRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return MobSpawn01(self.ctx)
        if self.random_condition(rate=10):
            return MobSpawn02(self.ctx)
        if self.random_condition(rate=10):
            return MobSpawn03(self.ctx)
        if self.random_condition(rate=10):
            return MobSpawn04(self.ctx)
        if self.random_condition(rate=10):
            return MobSpawn05(self.ctx)
        if self.random_condition(rate=10):
            return MobSpawn06(self.ctx)
        if self.random_condition(rate=10):
            return MobSpawn07(self.ctx)
        if self.random_condition(rate=10):
            return MobSpawn08(self.ctx)
        if self.random_condition(rate=10):
            return MobSpawn09(self.ctx)
        if self.random_condition(rate=10):
            return MobSpawn10(self.ctx)
        if self.user_value(key='ExtraEventOff', value=1):
            return Quit(self.ctx)


class MobSpawn01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1200], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1200]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1201], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1201]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1202]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1203], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1203]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn05(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1204], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1204]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn06(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1205], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1205]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn07(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1206], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1206]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn08(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1207], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1207]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn09(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1208], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1208]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1209], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1209]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class Notice(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=16, key='RelicMobSkyblueDie', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209])


initial_state = Setting
