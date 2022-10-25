""" trigger/02100001_bf/11_guidenpcspawn.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[109])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9903]):
            return NpcSpawn(self.ctx)


class NpcSpawn(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[109], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=60000):
            return CheckUser(self.ctx)


class CheckUser(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9903]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[109])


initial_state = Wait
