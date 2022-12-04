""" trigger/99999883/testtrigger4.xml """
import trigger_api


class START(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2001]):
            return idle(self.ctx)


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)


initial_state = START
