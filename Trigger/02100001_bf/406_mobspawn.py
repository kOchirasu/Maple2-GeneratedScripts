""" trigger/02100001_bf/406_mobspawn.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='RemoveAll', value=0)
        self.destroy_monster(spawnIds=[406])

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return MobSpawn(self.ctx)


class MobSpawn(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[406], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[406]):
            return Delay01(self.ctx)
        if self.user_value(key='RemoveAll', value=1):
            return Quit(self.ctx)


class Delay01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=60000):
            return MobSpawn(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[406])


initial_state = Wait
