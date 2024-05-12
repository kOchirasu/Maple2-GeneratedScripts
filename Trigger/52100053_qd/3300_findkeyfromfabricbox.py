""" trigger/52100053_qd/3300_findkeyfromfabricbox.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3300], visible=False, start_delay=0, interval=0, fade=0) # FindKeyFromFabricbox
        self.set_mesh(trigger_ids=[3301], visible=True, start_delay=0, interval=0, fade=0) # Fabricbox
        self.set_interact_object(trigger_ids=[10002093], state=0) # Fabricbox
        self.set_user_value(key='FindKey', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindKey', value=1):
            return StateTrue(self.ctx)
        if self.user_value(key='FindKey', value=2):
            return StateFalse(self.ctx)


class StateTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3301], visible=False, start_delay=100, interval=0, fade=2) # Fabricbox
        self.set_interact_object(trigger_ids=[10002093], state=1) # Fabricbox

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002093], state=0):
            return KeyFound(self.ctx)


class KeyFound(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3300], visible=True, start_delay=0, interval=0, fade=2) # FindKeyFromFabricbox
        self.set_user_value(trigger_id=1, key='PortalOn', value=1)


class StateFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002093], state=1) # Fabricbox

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002093], state=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3301], visible=True, start_delay=0, interval=0, fade=0) # Fabricbox


initial_state = Wait
