""" trigger/02100001_bf/1203_flyaway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='FlyAway', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FlyAway', value=1):
            return FlyAway(self.ctx)


class FlyAway(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=203, addSpawnId=1203)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
