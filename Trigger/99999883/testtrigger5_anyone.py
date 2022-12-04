""" trigger/99999883/testtrigger5_anyone.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[901])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return StartDelay(self.ctx)


class StartDelay(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return CheckAnyOne(self.ctx)


class CheckAnyOne(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.any_one():
            return QuitDelay(self.ctx)


class QuitDelay(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[901])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait(self.ctx)


initial_state = Wait
