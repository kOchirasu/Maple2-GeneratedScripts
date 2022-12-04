""" trigger/02020017_bf/100003_timeevent_triggervalue.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='EventStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EventStart', value=1):
            return PuzzleOn(self.ctx)


class PuzzleOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='EventStart', value=0)
        self.set_user_value(triggerId=13000, key='TimeEventOn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_seconds_user_value(key='TimeEventLifeTime'):
            return PuzzleOff(self.ctx)


class PuzzleOff(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=13000, key='TimeEventOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
