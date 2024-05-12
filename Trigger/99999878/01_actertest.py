""" trigger/99999878/01_actertest.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=1000, visible=True, initialSequence='Closed')
        self.set_breakable(triggerIds=[2000], enable=False)
        self.set_visible_breakable_object(triggerIds=[2000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return OpenDelay(self.ctx)


class OpenDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Open(self.ctx)


class Open(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=1000, visible=True, initialSequence='Opened')
        self.set_breakable(triggerIds=[2000], enable=True)
        self.set_visible_breakable_object(triggerIds=[2000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return OffDelay(self.ctx)


class OffDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Off(self.ctx)


class Off(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=1000, visible=False, initialSequence='Opened')
        self.set_breakable(triggerIds=[2000], enable=False)
        self.set_visible_breakable_object(triggerIds=[2000], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait(self.ctx)


initial_state = Wait
