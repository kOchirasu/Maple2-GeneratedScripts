""" trigger/02100001_bf/1201_flyaway.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='FlyAway', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='FlyAway', value=1):
            return FlyAway(self.ctx)


class FlyAway(common.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=201, addSpawnId=1201)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1201])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
