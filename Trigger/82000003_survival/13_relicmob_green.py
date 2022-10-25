""" trigger/82000003_survival/13_relicmob_green.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1300,1301,1302,1303,1304,1305,1306,1307,1308,1309])
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
        self.create_monster(spawnIds=[1300], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1300]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1301], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1301]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1302], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1302]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1303], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1303]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn05(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1304], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1304]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn06(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1305], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1305]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn07(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1306], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1306]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn08(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1307], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1307]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn09(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1308], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1308]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1309], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1309]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class Notice(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=16, key='RelicMobGreenDie', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1300,1301,1302,1303,1304,1305,1306,1307,1308,1309])


initial_state = Setting
