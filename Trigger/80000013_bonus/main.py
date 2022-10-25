""" trigger/80000013_bonus/main.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return start(self.ctx)


class start(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[108], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=60000):
            return end(self.ctx)


class end(common.Trigger):
    pass


initial_state = idle
