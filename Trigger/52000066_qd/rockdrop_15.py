""" trigger/52000066_qd/rockdrop_15.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8011], enable=False)
        self.set_skill(triggerIds=[8012], enable=False)
        self.set_effect(triggerIds=[7011], visible=False) # RockDrop
        self.set_effect(triggerIds=[7012], visible=False) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return RockDrop01(self.ctx)


class RockDrop01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7011], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1200):
            return RockDrop02(self.ctx)


class RockDrop02(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8011], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return RockDrop11(self.ctx)


class RockDrop11(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7012], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1200):
            return RockDrop12(self.ctx)


class RockDrop12(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8012], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return RockDrop21(self.ctx)


class RockDrop21(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7011], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1200):
            return RockDrop22(self.ctx)


class RockDrop22(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8011], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8011], enable=False)
        self.set_skill(triggerIds=[8012], enable=False)
        self.set_effect(triggerIds=[7011], visible=False) # RockDrop
        self.set_effect(triggerIds=[7012], visible=False) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return RockDrop01(self.ctx)


initial_state = Wait
