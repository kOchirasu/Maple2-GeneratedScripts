""" trigger/66200001_gd/color_7320.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Color32', value=10)
        self.set_mesh(triggerIds=[832], visible=True, arg3=0, delay=0, scale=0) # yellow
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1032], visible=False, arg3=0, delay=0, scale=0) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorStart', value=1):
            return YellowBefore(self.ctx)


# Yellow Before
class YellowBefore(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[832], visible=True, arg3=0, delay=0, scale=2) # yellow
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1032], visible=False, arg3=0, delay=0, scale=0) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorClear', value=1):
            return Clear(self.ctx)
        if self.user_value(key='ColorReset', value=1):
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)
        if self.user_value(key='Color32', value=2):
            return GreenAfter(self.ctx)
        if self.user_value(key='Color32', value=3):
            return None # Missing State: YellowtoRed


# Red Before
class RedBefore(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[1032], visible=True, arg3=0, delay=0, scale=0) # red
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[832], visible=False, arg3=0, delay=0, scale=0) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorClear', value=1):
            return Clear(self.ctx)
        if self.user_value(key='ColorReset', value=1):
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)
        if self.user_value(key='Color32', value=1):
            return YellowAfter(self.ctx)
        if self.user_value(key='Color32', value=2):
            return GreenAfter(self.ctx)


# Green After
class GreenAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[932], visible=True, arg3=0, delay=0, scale=0) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorClear', value=1):
            return Clear(self.ctx)
        if self.user_value(key='ColorReset', value=1):
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)
        if self.user_value(key='Color32', value=1):
            return YellowAfter(self.ctx)
        if self.user_value(key='Color32', value=3):
            return RedAfter(self.ctx)


# Yellow After
class YellowAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[832], visible=True, arg3=0, delay=0, scale=2) # yellow
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1032], visible=False, arg3=100, delay=0, scale=0) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorClear', value=1):
            return Clear(self.ctx)
        if self.user_value(key='ColorReset', value=1):
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)
        if self.user_value(key='Color32', value=2):
            return GreenAfter(self.ctx)
        if self.user_value(key='Color32', value=3):
            return RedAfter(self.ctx)


# Red After
class RedAfter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[1032], visible=True, arg3=0, delay=0, scale=0) # red
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[832], visible=False, arg3=100, delay=0, scale=0) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorClear', value=1):
            return Clear(self.ctx)
        if self.user_value(key='ColorReset', value=1):
            return Reset(self.ctx)
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)
        if self.user_value(key='Color32', value=1):
            return YellowAfter(self.ctx)
        if self.user_value(key='Color32', value=2):
            return GreenAfter(self.ctx)


# All Clear
class Clear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=2) # green
        self.set_mesh(triggerIds=[832], visible=False, arg3=0, delay=0, scale=2) # yellow
        self.set_mesh(triggerIds=[1032], visible=False, arg3=0, delay=0, scale=2) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorEnd', value=1):
            return Regen(self.ctx)


# Regen
class Regen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger
        self.set_user_value(key='ColorEnd', value=0) # Main Trigger
        self.set_user_value(key='ColorReset', value=0) # Sensor Trigger
        self.set_user_value(key='ColorClear', value=0) # Sensor Trigger
        self.set_mesh(triggerIds=[832], visible=True, arg3=400, delay=0, scale=0) # yellow
        self.set_mesh(triggerIds=[932], visible=False, arg3=0, delay=0, scale=0) # green
        self.set_mesh(triggerIds=[1032], visible=False, arg3=0, delay=0, scale=0) # red

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


# Reset
class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='ColorStart', value=0) # Pattern Trigger
        self.set_user_value(key='ColorReset', value=0) # Sensor Trigger
        self.set_user_value(key='ColorClear', value=0) # Sensor Trigger

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ColorEnd', value=1):
            return Wait(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(key='ColorEnd', value=0)
        # Main Trigger


initial_state = Wait
