""" trigger/52100051_qd/02_enteracemob.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[900,901]) # Mob_Enter
        self.set_user_value(key='MobSpawn', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MobSpawn', value=1):
            return MobSpawn01(self.ctx)


class MobSpawn01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[900], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return MobSpawn02(self.ctx)


class MobSpawn02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[900,901]):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return MobSpawn01(self.ctx)


initial_state = Setting
