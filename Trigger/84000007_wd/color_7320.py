""" trigger/84000007_wd/color_7320.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='Color32', value=10)
        self.set_mesh(triggerIds=[832], visible=True, arg3=0, delay=0, scale=0) # yellow
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1032], visible=False, arg3=0, delay=0, scale=0) # red

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ColorStart', value=1):
            return YellowBefore(self.ctx)
        if self.user_value(key='ColorStart', value=6):
            return RedBefore(self.ctx)


# Yellow Before
class YellowBefore(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[832], visible=True, arg3=0, delay=0, scale=2) # yellow
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1032], visible=False, arg3=0, delay=0, scale=0) # red

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Color32', value=2):
            return GreenAfter(self.ctx)
        if self.user_value(key='Color32', value=3):
            return None # Missing State: YellowtoRed
        if self.user_value(key='Color32', value=4):
            return Clear(self.ctx)
        if self.user_value(key='Color32', value=0):
            return Reset(self.ctx)
        if self.user_value(key='Color32', value=5):
            return Regen(self.ctx)


# Red Before
class RedBefore(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1032], visible=True, arg3=0, delay=0, scale=0) # red
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[832], visible=False, arg3=0, delay=0, scale=0) # yellow

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Color32', value=1):
            return YellowAfter(self.ctx)
        if self.user_value(key='Color32', value=2):
            return GreenAfter(self.ctx)
        if self.user_value(key='Color32', value=4):
            return Clear(self.ctx)
        if self.user_value(key='Color32', value=0):
            return Reset(self.ctx)
        if self.user_value(key='Color32', value=5):
            return Regen(self.ctx)


# Green After
class GreenAfter(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[932], visible=True, arg3=0, delay=0, scale=0) # green

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Color32', value=1):
            return YellowAfter(self.ctx)
        if self.user_value(key='Color32', value=3):
            return RedAfter(self.ctx)
        if self.user_value(key='Color32', value=4):
            return Clear(self.ctx)
        if self.user_value(key='Color32', value=0):
            return Reset(self.ctx)
        if self.user_value(key='Color32', value=5):
            return Regen(self.ctx)


# Yellow After
class YellowAfter(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[832], visible=True, arg3=0, delay=0, scale=2) # yellow
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1032], visible=False, arg3=100, delay=0, scale=0) # red

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Color32', value=2):
            return GreenAfter(self.ctx)
        if self.user_value(key='Color32', value=3):
            return RedAfter(self.ctx)
        if self.user_value(key='Color32', value=4):
            return Clear(self.ctx)
        if self.user_value(key='Color32', value=0):
            return Reset(self.ctx)
        if self.user_value(key='Color32', value=5):
            return Regen(self.ctx)


# Red After
class RedAfter(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1032], visible=True, arg3=0, delay=0, scale=0) # red
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[832], visible=False, arg3=100, delay=0, scale=0) # yellow

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Color32', value=1):
            return YellowAfter(self.ctx)
        if self.user_value(key='Color32', value=2):
            return GreenAfter(self.ctx)
        if self.user_value(key='Color32', value=4):
            return Clear(self.ctx)
        if self.user_value(key='Color32', value=0):
            return Reset(self.ctx)
        if self.user_value(key='Color32', value=5):
            return Regen(self.ctx)


# All Clear
class Clear(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=2) # green
        self.set_mesh(triggerIds=[832], visible=False, arg3=0, delay=0, scale=2) # yellow
        self.set_mesh(triggerIds=[1032], visible=False, arg3=0, delay=0, scale=2) # red

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Color32', value=5):
            return Regen(self.ctx)


# Regen
class Regen(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger
        self.set_mesh(triggerIds=[832], visible=True, arg3=400, delay=0, scale=0) # yellow
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1032], visible=False, arg3=0, delay=0, scale=0) # red

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


# Reset
class Reset(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Color32', value=5):
            return Wait(self.ctx)


initial_state = Wait
