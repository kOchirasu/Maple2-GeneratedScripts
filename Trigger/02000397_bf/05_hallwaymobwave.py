""" trigger/02000397_bf/05_hallwaymobwave.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[930,931,932,933]) # Mob
        self.set_user_value(key='MobWave', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MobWave', value=1):
            return MobSpawn01(self.ctx)


class MobSpawn01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[930], animationEffect=False) # Mob

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return MobSpawn02(self.ctx)


class MobSpawn02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[931], animationEffect=False) # Mob

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return MobSpawn03(self.ctx)


class MobSpawn03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[932], animationEffect=False) # Mob

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return MobSpawn04(self.ctx)


class MobSpawn04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[933], animationEffect=False) # Mob


initial_state = Setting
