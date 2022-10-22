""" trigger/66200001_gd/color_7130.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='Color13', value=10)
        set_mesh(triggerIds=[813], visible=True, arg3=0, arg4=0, arg5=0) # yellow
        set_mesh(triggerIds=[913], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[1013], visible=False, arg3=0, arg4=0, arg5=0) # red

    def on_tick(self) -> state.State:
        if user_value(key='ColorStart', value=1):
            return YellowBefore()


#  Yellow Before 
class YellowBefore(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[813], visible=True, arg3=0, arg4=0, arg5=2) # yellow
        set_mesh(triggerIds=[913], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[1013], visible=False, arg3=0, arg4=0, arg5=0) # red

    def on_tick(self) -> state.State:
        if user_value(key='ColorClear', value=1):
            return Clear()
        if user_value(key='ColorReset', value=1):
            return Reset()
        if user_value(key='ColorEnd', value=1):
            return Regen()
        if user_value(key='Color13', value=2):
            return GreenAfter()
        if user_value(key='Color13', value=3):
            return None # Missing State: YellowtoRed


#  Red Before 
class RedBefore(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1013], visible=True, arg3=0, arg4=0, arg5=0) # red
        set_mesh(triggerIds=[913], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[813], visible=False, arg3=0, arg4=0, arg5=0) # yellow

    def on_tick(self) -> state.State:
        if user_value(key='ColorClear', value=1):
            return Clear()
        if user_value(key='ColorReset', value=1):
            return Reset()
        if user_value(key='ColorEnd', value=1):
            return Regen()
        if user_value(key='Color13', value=1):
            return YellowAfter()
        if user_value(key='Color13', value=2):
            return GreenAfter()


#  Green After 
class GreenAfter(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[913], visible=True, arg3=0, arg4=0, arg5=0) # green

    def on_tick(self) -> state.State:
        if user_value(key='ColorClear', value=1):
            return Clear()
        if user_value(key='ColorReset', value=1):
            return Reset()
        if user_value(key='ColorEnd', value=1):
            return Regen()
        if user_value(key='Color13', value=1):
            return YellowAfter()
        if user_value(key='Color13', value=3):
            return RedAfter()


#  Yellow After 
class YellowAfter(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[813], visible=True, arg3=0, arg4=0, arg5=2) # yellow
        set_mesh(triggerIds=[913], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[1013], visible=False, arg3=100, arg4=0, arg5=0) # red

    def on_tick(self) -> state.State:
        if user_value(key='ColorClear', value=1):
            return Clear()
        if user_value(key='ColorReset', value=1):
            return Reset()
        if user_value(key='ColorEnd', value=1):
            return Regen()
        if user_value(key='Color13', value=2):
            return GreenAfter()
        if user_value(key='Color13', value=3):
            return RedAfter()


#  Red After 
class RedAfter(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1013], visible=True, arg3=0, arg4=0, arg5=0) # red
        set_mesh(triggerIds=[913], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[813], visible=False, arg3=100, arg4=0, arg5=0) # yellow

    def on_tick(self) -> state.State:
        if user_value(key='ColorClear', value=1):
            return Clear()
        if user_value(key='ColorReset', value=1):
            return Reset()
        if user_value(key='ColorEnd', value=1):
            return Regen()
        if user_value(key='Color13', value=1):
            return YellowAfter()
        if user_value(key='Color13', value=2):
            return GreenAfter()


#  All Clear 
class Clear(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[913], visible=False, arg3=0, arg4=0, arg5=2) # green
        set_mesh(triggerIds=[813], visible=False, arg3=0, arg4=0, arg5=2) # yellow
        set_mesh(triggerIds=[1013], visible=False, arg3=0, arg4=0, arg5=2) # red

    def on_tick(self) -> state.State:
        if user_value(key='ColorEnd', value=1):
            return Regen()


#  Regen 
class Regen(state.State):
    def on_enter(self):
        set_user_value(key='ColorStart', value=0) # Pattern Trigger
        set_user_value(key='ColorEnd', value=0) # Main Trigger
        set_user_value(key='ColorReset', value=0) # Sensor Trigger
        set_user_value(key='ColorClear', value=0) # Sensor Trigger
        set_mesh(triggerIds=[813], visible=True, arg3=400, arg4=0, arg5=0) # yellow
        set_mesh(triggerIds=[913], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[1013], visible=False, arg3=0, arg4=0, arg5=0) # red

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


#  Reset 
class Reset(state.State):
    def on_enter(self):
        set_user_value(key='ColorStart', value=0) # Pattern Trigger
        set_user_value(key='ColorReset', value=0) # Sensor Trigger
        set_user_value(key='ColorClear', value=0) # Sensor Trigger

    def on_tick(self) -> state.State:
        if user_value(key='ColorEnd', value=1):
            return Wait()

    def on_exit(self):
        set_user_value(key='ColorEnd', value=0) # Main Trigger


