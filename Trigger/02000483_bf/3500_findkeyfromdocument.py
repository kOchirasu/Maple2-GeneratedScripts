""" trigger/02000483_bf/3500_findkeyfromdocument.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3500], visible=False, arg3=0, arg4=0, arg5=0) # FindKeyFromDocument
        set_mesh(triggerIds=[3501], visible=True, arg3=0, arg4=0, arg5=0) # Document
        set_interact_object(triggerIds=[10002042], state=0) # Document
        set_user_value(key='FindKey', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindKey', value=1):
            return True()
        if user_value(key='FindKey', value=2):
            return False()


class True(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3501], visible=False, arg3=100, arg4=0, arg5=2) # Document
        set_interact_object(triggerIds=[10002042], state=1) # Document

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002042], arg2=0):
            return KeyFound()


class KeyFound(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3500], visible=True, arg3=0, arg4=0, arg5=2) # FindKeyFromDocument
        set_user_value(triggerId=1, key='PortalOn', value=1)


class False(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002042], state=1) # Document

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002042], arg2=0):
            return NothingHappened()


class NothingHappened(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3501], visible=True, arg3=0, arg4=0, arg5=0) # Document


