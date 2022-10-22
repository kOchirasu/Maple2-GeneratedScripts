""" trigger/84000007_wd/color_7320.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='Color32', value=10)
        set_mesh(triggerIds=[832], visible=True, arg3=0, arg4=0, arg5=0) # yellow
        set_mesh(triggerIds=[932], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[1032], visible=False, arg3=0, arg4=0, arg5=0) # red

    def on_tick(self) -> state.State:
        if user_value(key='ColorStart', value=1):
            return YellowBefore()
        if user_value(key='ColorStart', value=6):
            return RedBefore()


#  Yellow Before 
class YellowBefore(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[832], visible=True, arg3=0, arg4=0, arg5=2) # yellow
        set_mesh(triggerIds=[932], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[1032], visible=False, arg3=0, arg4=0, arg5=0) # red

    def on_tick(self) -> state.State:
        if user_value(key='Color32', value=2):
            return GreenAfter()
        if user_value(key='Color32', value=3):
            return None # Missing State: YellowtoRed
        if user_value(key='Color32', value=4):
            return Clear()
        if user_value(key='Color32', value=0):
            return Reset()
        if user_value(key='Color32', value=5):
            return Regen()


#  Red Before 
class RedBefore(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1032], visible=True, arg3=0, arg4=0, arg5=0) # red
        set_mesh(triggerIds=[932], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[832], visible=False, arg3=0, arg4=0, arg5=0) # yellow

    def on_tick(self) -> state.State:
        if user_value(key='Color32', value=1):
            return YellowAfter()
        if user_value(key='Color32', value=2):
            return GreenAfter()
        if user_value(key='Color32', value=4):
            return Clear()
        if user_value(key='Color32', value=0):
            return Reset()
        if user_value(key='Color32', value=5):
            return Regen()


#  Green After 
class GreenAfter(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[932], visible=True, arg3=0, arg4=0, arg5=0) # green

    def on_tick(self) -> state.State:
        if user_value(key='Color32', value=1):
            return YellowAfter()
        if user_value(key='Color32', value=3):
            return RedAfter()
        if user_value(key='Color32', value=4):
            return Clear()
        if user_value(key='Color32', value=0):
            return Reset()
        if user_value(key='Color32', value=5):
            return Regen()


#  Yellow After 
class YellowAfter(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[832], visible=True, arg3=0, arg4=0, arg5=2) # yellow
        set_mesh(triggerIds=[932], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[1032], visible=False, arg3=100, arg4=0, arg5=0) # red

    def on_tick(self) -> state.State:
        if user_value(key='Color32', value=2):
            return GreenAfter()
        if user_value(key='Color32', value=3):
            return RedAfter()
        if user_value(key='Color32', value=4):
            return Clear()
        if user_value(key='Color32', value=0):
            return Reset()
        if user_value(key='Color32', value=5):
            return Regen()


#  Red After 
class RedAfter(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1032], visible=True, arg3=0, arg4=0, arg5=0) # red
        set_mesh(triggerIds=[932], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[832], visible=False, arg3=100, arg4=0, arg5=0) # yellow

    def on_tick(self) -> state.State:
        if user_value(key='Color32', value=1):
            return YellowAfter()
        if user_value(key='Color32', value=2):
            return GreenAfter()
        if user_value(key='Color32', value=4):
            return Clear()
        if user_value(key='Color32', value=0):
            return Reset()
        if user_value(key='Color32', value=5):
            return Regen()


#  All Clear 
class Clear(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[932], visible=False, arg3=0, arg4=0, arg5=2) # green
        set_mesh(triggerIds=[832], visible=False, arg3=0, arg4=0, arg5=2) # yellow
        set_mesh(triggerIds=[1032], visible=False, arg3=0, arg4=0, arg5=2) # red

    def on_tick(self) -> state.State:
        if user_value(key='Color32', value=5):
            return Regen()


#  Regen 
class Regen(state.State):
    def on_enter(self):
        set_user_value(key='ColorStart', value=0) # Pattern Trigger
        set_mesh(triggerIds=[832], visible=True, arg3=400, arg4=0, arg5=0) # yellow
        set_mesh(triggerIds=[932], visible=False, arg3=0, arg4=0, arg5=0) # green
        set_mesh(triggerIds=[1032], visible=False, arg3=0, arg4=0, arg5=0) # red

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


#  Reset 
class Reset(state.State):
    def on_enter(self):
        set_user_value(key='ColorStart', value=0) # Pattern Trigger

    def on_tick(self) -> state.State:
        if user_value(key='Color32', value=5):
            return Wait()


