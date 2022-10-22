""" trigger/52100053_qd/3400_findkeyfromcandle.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3400], visible=False, arg3=0, arg4=0, arg5=0) # FindKeyFromCandle
        set_mesh(triggerIds=[3401], visible=True, arg3=0, arg4=0, arg5=0) # Candle
        set_interact_object(triggerIds=[10002094], state=0) # Candle
        set_user_value(key='FindKey', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindKey', value=1):
            return True()
        if user_value(key='FindKey', value=2):
            return False()


class True(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3401], visible=False, arg3=100, arg4=0, arg5=2) # Candle
        set_interact_object(triggerIds=[10002094], state=1) # Candle

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002094], arg2=0):
            return KeyFound()


class KeyFound(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3400], visible=True, arg3=0, arg4=0, arg5=2) # FindKeyFromCandle
        set_user_value(triggerId=1, key='PortalOn', value=1)


class False(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002094], state=1) # Candle

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002094], arg2=0):
            return NothingHappened()


class NothingHappened(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3401], visible=True, arg3=0, arg4=0, arg5=0) # Fabricbox


