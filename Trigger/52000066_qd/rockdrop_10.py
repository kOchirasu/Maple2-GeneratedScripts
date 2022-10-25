""" trigger/52000066_qd/rockdrop_10.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8000], enable=False)
        self.set_skill(triggerIds=[8001], enable=False)
        self.set_effect(triggerIds=[7000], visible=False) # RockDrop
        self.set_effect(triggerIds=[7001], visible=False) # RockDrop

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return RockDrop01(self.ctx)


class RockDrop01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7000], visible=True) # RockDrop

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return RockDrop02(self.ctx)


class RockDrop02(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8000], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return RockDrop11(self.ctx)


class RockDrop11(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7001], visible=True) # RockDrop

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return RockDrop12(self.ctx)


class RockDrop12(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8001], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return RockDrop21(self.ctx)


class RockDrop21(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7000], visible=True) # RockDrop

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return RockDrop22(self.ctx)


class RockDrop22(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8000], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8000], enable=False)
        self.set_skill(triggerIds=[8001], enable=False)
        self.set_effect(triggerIds=[7000], visible=False) # RockDrop
        self.set_effect(triggerIds=[7001], visible=False) # RockDrop

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return RockDrop01(self.ctx)


initial_state = Wait
