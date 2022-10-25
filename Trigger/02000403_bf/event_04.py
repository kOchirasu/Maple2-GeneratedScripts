""" trigger/02000403_bf/event_04.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1803], visible=True, arg3=0, delay=200, scale=0)
        self.set_mesh(triggerIds=[1804], visible=False, arg3=0, delay=200, scale=0)
        self.set_mesh(triggerIds=[1805], visible=False, arg3=0, delay=200, scale=0)
        self.set_mesh(triggerIds=[1806], visible=False, arg3=0, delay=200, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[705]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1803], visible=False, arg3=0, delay=200, scale=85)
        self.set_mesh(triggerIds=[1804], visible=True, arg3=0, delay=200, scale=85)
        self.set_mesh(triggerIds=[1805], visible=False, arg3=0, delay=200, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return Ready_02(self.ctx)


class Ready_02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1803], visible=False, arg3=0, delay=200, scale=5)
        self.set_mesh(triggerIds=[1804], visible=True, arg3=0, delay=200, scale=5)
        self.set_mesh(triggerIds=[1806], visible=True, arg3=0, delay=200, scale=5)
        self.set_achievement(triggerId=705, type='trigger', achieve='Hauntedmansion')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Ready_03(self.ctx)


class Ready_03(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1806], visible=False, arg3=0, delay=200, scale=5)


initial_state = idle
