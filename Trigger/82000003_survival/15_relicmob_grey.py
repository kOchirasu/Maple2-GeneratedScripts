""" trigger/82000003_survival/15_relicmob_grey.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1500,1501,1502,1503,1504,1505,1506,1507,1508,1509])
        self.set_user_value(key='RelicMobSpawn', value=0)
        self.set_user_value(key='RelicMobRemove', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobSpawn', value=1):
            return Delay(self.ctx)


class Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            # 30초 30000
            return MobSpawnRandom(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawnRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1500], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1500]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1501], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1501]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1502], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1502]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1503], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1503]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1504], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1504]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1505], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1505]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1506], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1506]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1507], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1507]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1508], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1508]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class MobSpawn10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1509], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1509]):
            return Notice(self.ctx)
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class Notice(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=16, key='RelicMobGreyDie', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRemove', value=1):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1500,1501,1502,1503,1504,1505,1506,1507,1508,1509])


initial_state = Setting
