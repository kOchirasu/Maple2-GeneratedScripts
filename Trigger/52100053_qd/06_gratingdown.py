""" trigger/52100053_qd/06_gratingdown.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002104], state=0) # Lever_BlockStart
        self.set_interact_object(triggerIds=[10002105], state=0) # Lever_BlockOff
        self.set_mesh(triggerIds=[6200,6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211], visible=False, arg3=0, delay=0, scale=0) # GratingDown
        self.set_mesh(triggerIds=[6300,6301,6302,6303,6304,6305], visible=True, arg3=0, delay=0, scale=0) # GratingUp
        self.set_mesh(triggerIds=[3901], visible=False, arg3=0, delay=0, scale=0) # InvisibleBarrier_TOKfalse
        self.set_breakable(triggerIds=[6000], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6001], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6002], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6003], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6004], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6005], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6006], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6007], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6008], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6009], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6010], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6011], enable=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6000], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6001], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6002], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6003], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6004], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6005], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6006], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6007], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6008], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6009], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6010], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6011], visible=False) # Grating_Start
        self.set_breakable(triggerIds=[6100], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6101], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6102], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6103], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6104], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6105], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6106], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6107], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6108], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6109], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6110], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6111], enable=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6100], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6101], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6102], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6103], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6104], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6105], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6106], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6107], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6108], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6109], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6110], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6111], visible=False) # Grating_Off
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_user_value(key='BlockEnable', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BlockEnable', value=1):
            return BlockEnable(self.ctx)


class BlockEnable(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002104], state=1) # Lever_BlockStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002104], stateValue=0):
            return BlockStart(self.ctx)


class BlockStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6300,6301,6302,6303,6304,6305], visible=False, arg3=100, delay=0, scale=2) # GratingUp
        self.set_breakable(triggerIds=[6000], enable=True) # Grating_Start
        self.set_breakable(triggerIds=[6001], enable=True) # Grating_Start
        self.set_breakable(triggerIds=[6002], enable=True) # Grating_Start
        self.set_breakable(triggerIds=[6003], enable=True) # Grating_Start
        self.set_breakable(triggerIds=[6004], enable=True) # Grating_Start
        self.set_breakable(triggerIds=[6005], enable=True) # Grating_Start
        self.set_breakable(triggerIds=[6006], enable=True) # Grating_Start
        self.set_breakable(triggerIds=[6007], enable=True) # Grating_Start
        self.set_breakable(triggerIds=[6008], enable=True) # Grating_Start
        self.set_breakable(triggerIds=[6009], enable=True) # Grating_Start
        self.set_breakable(triggerIds=[6010], enable=True) # Grating_Start
        self.set_breakable(triggerIds=[6011], enable=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6000], visible=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6001], visible=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6002], visible=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6003], visible=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6004], visible=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6005], visible=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6006], visible=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6007], visible=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6008], visible=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6009], visible=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6010], visible=True) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6011], visible=True) # Grating_Start

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BlockIng(self.ctx)


class BlockIng(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3901], visible=True, arg3=0, delay=0, scale=0) # InvisibleBarrier_TOKfalse
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return BlockEnd(self.ctx)


class BlockEnd(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6200,6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211], visible=True, arg3=0, delay=0, scale=0) # GratingDown
        self.set_breakable(triggerIds=[6000], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6001], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6002], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6003], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6004], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6005], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6006], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6007], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6008], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6009], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6010], enable=False) # Grating_Start
        self.set_breakable(triggerIds=[6011], enable=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6000], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6001], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6002], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6003], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6004], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6005], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6006], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6007], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6008], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6009], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6010], visible=False) # Grating_Start
        self.set_visible_breakable_object(triggerIds=[6011], visible=False) # Grating_Start

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return BlockDisable(self.ctx)


class BlockDisable(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002105], state=1) # Lever_BlockOff

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002105], stateValue=0):
            return BlockOffStart(self.ctx)


class BlockOffStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6200,6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211], visible=False, arg3=100, delay=0, scale=2) # GratingDown
        self.set_breakable(triggerIds=[6100], enable=True) # Grating_Off
        self.set_breakable(triggerIds=[6101], enable=True) # Grating_Off
        self.set_breakable(triggerIds=[6102], enable=True) # Grating_Off
        self.set_breakable(triggerIds=[6103], enable=True) # Grating_Off
        self.set_breakable(triggerIds=[6104], enable=True) # Grating_Off
        self.set_breakable(triggerIds=[6105], enable=True) # Grating_Off
        self.set_breakable(triggerIds=[6106], enable=True) # Grating_Off
        self.set_breakable(triggerIds=[6107], enable=True) # Grating_Off
        self.set_breakable(triggerIds=[6108], enable=True) # Grating_Off
        self.set_breakable(triggerIds=[6109], enable=True) # Grating_Off
        self.set_breakable(triggerIds=[6110], enable=True) # Grating_Off
        self.set_breakable(triggerIds=[6111], enable=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6100], visible=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6101], visible=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6102], visible=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6103], visible=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6104], visible=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6105], visible=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6106], visible=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6107], visible=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6108], visible=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6109], visible=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6110], visible=True) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6111], visible=True) # Grating_Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BlockOffIng(self.ctx)


class BlockOffIng(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3901], visible=False, arg3=0, delay=0, scale=0) # InvisibleBarrier_TOKfalse
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return BlockOffEnd(self.ctx)


class BlockOffEnd(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6300,6301,6302,6303,6304,6305], visible=True, arg3=0, delay=0, scale=0) # GratingUp
        self.set_breakable(triggerIds=[6100], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6101], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6102], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6103], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6104], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6105], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6106], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6107], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6108], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6109], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6110], enable=False) # Grating_Off
        self.set_breakable(triggerIds=[6111], enable=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6100], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6101], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6102], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6103], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6104], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6105], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6106], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6107], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6108], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6109], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6110], visible=False) # Grating_Off
        self.set_visible_breakable_object(triggerIds=[6111], visible=False) # Grating_Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return BlockEnable(self.ctx)


initial_state = Setting
