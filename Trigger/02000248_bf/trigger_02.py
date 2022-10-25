""" trigger/02000248_bf/trigger_02.xml """
import common


class ready(common.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[2101,2102,2103,2104,2105], isVisible=True)


class objectset(common.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[2101,2102,2103,2104,2105], randomCount=1, isVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return WaitTick(self.ctx)


class WaitTick(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return objectset(self.ctx)


initial_state = ready
