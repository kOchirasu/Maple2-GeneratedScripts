""" trigger/52000073_qd/hiddendoor02.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3000, visible=True, initialSequence='Closed') # HiddenDoor
        self.set_mesh(triggerIds=[2000], visible=True, arg3=0, delay=0, scale=0) # Wall
        self.set_breakable(triggerIds=[4000], enable=False) # Move
        self.set_visible_breakable_object(triggerIds=[4000], visible=False) # Move
        self.set_interact_object(triggerIds=[10001082], state=1) # BookCase
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001082], stateValue=0):
            return BookCaseMove01(self.ctx)


class BookCaseMove01(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[4000], enable=True) # Move
        self.set_visible_breakable_object(triggerIds=[4000], visible=True) # Move
        self.set_mesh(triggerIds=[2000], visible=False, arg3=0, delay=0, scale=3) # Wall

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DoorOpen01(self.ctx)


class DoorOpen01(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3000, visible=True, initialSequence='Opened') # HiddenDoor
        self.set_portal(portalId=2, visible=True, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DoorOpen02(self.ctx)


class DoorOpen02(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=57000):
            return DoorClose01(self.ctx)


class DoorClose01(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3000, visible=True, initialSequence='Closed') # HiddenDoor
        self.set_portal(portalId=2, visible=True, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DoorClose02(self.ctx)


class DoorClose02(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[4000], enable=False) # Move
        self.set_visible_breakable_object(triggerIds=[4000], visible=False) # Move
        self.set_mesh(triggerIds=[2000], visible=True, arg3=0, delay=0, scale=3) # Wall
        self.set_interact_object(triggerIds=[10001082], state=1) # BookCase
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001082], stateValue=0):
            return BookCaseMove01(self.ctx)


initial_state = Wait
