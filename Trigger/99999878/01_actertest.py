""" trigger/99999878/01_actertest.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=1000, visible=True, initialSequence='Closed')
        self.set_breakable(triggerIds=[2000], enable=False)
        self.set_visible_breakable_object(triggerIds=[2000], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return OpenDelay(self.ctx)


class OpenDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Open(self.ctx)


class Open(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=1000, visible=True, initialSequence='Opened')
        self.set_breakable(triggerIds=[2000], enable=True)
        self.set_visible_breakable_object(triggerIds=[2000], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return OffDelay(self.ctx)


class OffDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Off(self.ctx)


class Off(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=1000, visible=False, initialSequence='Opened')
        self.set_breakable(triggerIds=[2000], enable=False)
        self.set_visible_breakable_object(triggerIds=[2000], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait(self.ctx)


initial_state = Wait
