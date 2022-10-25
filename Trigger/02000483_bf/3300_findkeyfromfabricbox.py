""" trigger/02000483_bf/3300_findkeyfromfabricbox.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3300], visible=False, arg3=0, delay=0, scale=0) # FindKeyFromFabricbox
        self.set_mesh(triggerIds=[3301], visible=True, arg3=0, delay=0, scale=0) # Fabricbox
        self.set_interact_object(triggerIds=[10002040], state=0) # Fabricbox
        self.set_user_value(key='FindKey', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='FindKey', value=1):
            return True(self.ctx)
        if self.user_value(key='FindKey', value=2):
            return False(self.ctx)


class True(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3301], visible=False, arg3=100, delay=0, scale=2) # Fabricbox
        self.set_interact_object(triggerIds=[10002040], state=1) # Fabricbox

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002040], stateValue=0):
            return KeyFound(self.ctx)


class KeyFound(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3300], visible=True, arg3=0, delay=0, scale=2) # FindKeyFromFabricbox
        self.set_user_value(triggerId=1, key='PortalOn', value=1)


class False(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002040], state=1) # Fabricbox

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002040], stateValue=0):
            return NothingHappened(self.ctx)


class NothingHappened(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3301], visible=True, arg3=0, delay=0, scale=0) # Fabricbox


initial_state = Wait
