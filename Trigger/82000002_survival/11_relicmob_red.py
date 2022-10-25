""" trigger/82000002_survival/11_relicmob_red.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109])
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
        self.create_monster(spawnIds=[1100], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1100]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1101], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1101]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1102], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1102]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1103], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1103]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn05(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1104], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1104]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn06(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1105], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1105]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn07(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1106], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1106]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn08(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1107], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1107]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn09(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1108], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1108]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1109], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1109]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class Notice(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=16, key='RelicMobRedDie', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109])


initial_state = Setting
