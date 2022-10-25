""" trigger/99999883/testtrigger4.xml """
import common


class START(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2001]):
            return idle(self.ctx)


class idle(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)


initial_state = START
