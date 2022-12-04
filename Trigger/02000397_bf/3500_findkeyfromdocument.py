""" trigger/02000397_bf/3500_findkeyfromdocument.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3500], visible=False, arg3=0, delay=0, scale=0) # FindKeyFromDocument
        self.set_mesh(triggerIds=[3501], visible=True, arg3=0, delay=0, scale=0) # Document
        self.set_interact_object(triggerIds=[10001144], state=0) # Document
        self.set_user_value(key='FindKey', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindKey', value=1):
            return True(self.ctx)
        if self.user_value(key='FindKey', value=2):
            return False(self.ctx)


class True(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3501], visible=False, arg3=100, delay=0, scale=2) # Document
        self.set_interact_object(triggerIds=[10001144], state=1) # Document

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001144], stateValue=0):
            return KeyFound(self.ctx)


class KeyFound(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3500], visible=True, arg3=0, delay=0, scale=2) # FindKeyFromDocument
        self.set_user_value(triggerId=1, key='PortalOn', value=1)


class False(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001144], state=1) # Document

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001144], stateValue=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3501], visible=True, arg3=0, delay=0, scale=0) # Document


initial_state = Wait
