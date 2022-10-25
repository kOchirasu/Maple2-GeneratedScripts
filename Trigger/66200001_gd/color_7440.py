""" trigger/66200001_gd/color_7440.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='Color44', value=10)
        self.set_mesh(triggerIds=[844], visible=True, arg3=0, delay=0, scale=0) # yellow
        self.set_mesh(triggerIds=[944], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1044], visible=False, arg3=0, delay=0, scale=0) # red

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ColorStart', value=1):
            return YellowBefore(self.ctx)


# Yellow Before
class YellowBefore(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[844], visible=True, arg3=0, delay=0, scale=2) # yellow
        self.set_mesh(triggerIds=[944], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1044], visible=False, arg3=0, delay=0, scale=0) # red

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ColorClear', value=1):
            return Clear(self.ctx)
        if self.user_value(key='ColorReset', value=1):
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)
        if self.user_value(key='Color44', value=2):
            return GreenAfter(self.ctx)
        if self.user_value(key='Color44', value=3):
            return None # Missing State: YellowtoRed


# Red Before
class RedBefore(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1044], visible=True, arg3=0, delay=0, scale=0) # red
        self.set_mesh(triggerIds=[944], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[844], visible=False, arg3=0, delay=0, scale=0) # yellow

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ColorClear', value=1):
            return Clear(self.ctx)
        if self.user_value(key='ColorReset', value=1):
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)
        if self.user_value(key='Color44', value=1):
            return YellowAfter(self.ctx)
        if self.user_value(key='Color44', value=2):
            return GreenAfter(self.ctx)


# Green After
class GreenAfter(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[944], visible=True, arg3=0, delay=0, scale=0) # green

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ColorClear', value=1):
            return Clear(self.ctx)
        if self.user_value(key='ColorReset', value=1):
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)
        if self.user_value(key='Color44', value=1):
            return YellowAfter(self.ctx)
        if self.user_value(key='Color44', value=3):
            return RedAfter(self.ctx)


# Yellow After
class YellowAfter(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[844], visible=True, arg3=0, delay=0, scale=2) # yellow
        self.set_mesh(triggerIds=[944], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1044], visible=False, arg3=100, delay=0, scale=0) # red

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ColorClear', value=1):
            return Clear(self.ctx)
        if self.user_value(key='ColorReset', value=1):
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)
        if self.user_value(key='Color44', value=2):
            return GreenAfter(self.ctx)
        if self.user_value(key='Color44', value=3):
            return RedAfter(self.ctx)


# Red After
class RedAfter(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1044], visible=True, arg3=0, delay=0, scale=0) # red
        self.set_mesh(triggerIds=[944], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[844], visible=False, arg3=100, delay=0, scale=0) # yellow

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ColorClear', value=1):
            return Clear(self.ctx)
        if self.user_value(key='ColorReset', value=1):
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)
        if self.user_value(key='Color44', value=1):
            return YellowAfter(self.ctx)
        if self.user_value(key='Color44', value=2):
            return GreenAfter(self.ctx)


# All Clear
class Clear(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[944], visible=False, arg3=0, delay=0, scale=2) # green
        self.set_mesh(triggerIds=[844], visible=False, arg3=0, delay=0, scale=2) # yellow
        self.set_mesh(triggerIds=[1044], visible=False, arg3=0, delay=0, scale=2) # red

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)


# Regen
class Regen(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger
        self.set_user_value(key='ColorEnd', value=0) # Main Trigger
        self.set_user_value(key='ColorReset', value=0) # Sensor Trigger
        self.set_user_value(key='ColorClear', value=0) # Sensor Trigger
        self.set_mesh(triggerIds=[844], visible=True, arg3=400, delay=0, scale=0) # yellow
        self.set_mesh(triggerIds=[944], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1044], visible=False, arg3=0, delay=0, scale=0) # red

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


# Reset
class Reset(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger
        self.set_user_value(key='ColorReset', value=0) # Sensor Trigger
        self.set_user_value(key='ColorClear', value=0) # Sensor Trigger

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ColorEnd', value=1):
            return Wait(self.ctx)

    def on_exit(self):
        self.set_user_value(key='ColorEnd', value=0) # Main Trigger


initial_state = Wait
