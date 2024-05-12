""" trigger/52100053_qd/3500_findkeyfromdocument.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3500], visible=False, arg3=0, delay=0, scale=0) # FindKeyFromDocument
        self.set_mesh(triggerIds=[3501], visible=True, arg3=0, delay=0, scale=0) # Document
        self.set_interact_object(triggerIds=[10002095], state=0) # Document
        self.set_user_value(key='FindKey', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindKey', value=1):
            return StateTrue(self.ctx)
        if self.user_value(key='FindKey', value=2):
            return StateFalse(self.ctx)


class StateTrue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3501], visible=False, arg3=100, delay=0, scale=2) # Document
        self.set_interact_object(triggerIds=[10002095], state=1) # Document

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002095], stateValue=0):
            return KeyFound(self.ctx)


class KeyFound(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3500], visible=True, arg3=0, delay=0, scale=2) # FindKeyFromDocument
        self.set_user_value(triggerId=1, key='PortalOn', value=1)


class StateFalse(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10002095], state=1) # Document

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002095], stateValue=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3501], visible=True, arg3=0, delay=0, scale=0) # Document


initial_state = Wait
