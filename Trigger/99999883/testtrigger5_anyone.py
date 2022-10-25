""" trigger/99999883/testtrigger5_anyone.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[901])

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return StartDelay(self.ctx)


class StartDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return CheckAnyOne(self.ctx)


class CheckAnyOne(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.any_one():
            return QuitDelay(self.ctx)


class QuitDelay(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[901])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait(self.ctx)


initial_state = Wait
