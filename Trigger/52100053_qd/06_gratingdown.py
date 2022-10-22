""" trigger/52100053_qd/06_gratingdown.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002104], state=0) # Lever_BlockStart
        set_interact_object(triggerIds=[10002105], state=0) # Lever_BlockOff
        set_mesh(triggerIds=[6200,6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211], visible=False, arg3=0, arg4=0, arg5=0) # GratingDown
        set_mesh(triggerIds=[6300,6301,6302,6303,6304,6305], visible=True, arg3=0, arg4=0, arg5=0) # GratingUp
        set_mesh(triggerIds=[3901], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleBarrier_TOKfalse
        set_breakable(triggerIds=[6000], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6001], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6002], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6003], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6004], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6005], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6006], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6007], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6008], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6009], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6010], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6011], enabled=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6000], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6001], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6002], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6003], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6004], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6005], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6006], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6007], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6008], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6009], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6010], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6011], arg2=False) # Grating_Start
        set_breakable(triggerIds=[6100], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6101], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6102], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6103], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6104], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6105], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6106], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6107], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6108], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6109], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6110], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6111], enabled=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6100], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6101], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6102], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6103], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6104], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6105], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6106], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6107], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6108], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6109], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6110], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6111], arg2=False) # Grating_Off
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_user_value(key='BlockEnable', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='BlockEnable', value=1):
            return BlockEnable()


class BlockEnable(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002104], state=1) # Lever_BlockStart

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002104], arg2=0):
            return BlockStart()


class BlockStart(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6300,6301,6302,6303,6304,6305], visible=False, arg3=100, arg4=0, arg5=2) # GratingUp
        set_breakable(triggerIds=[6000], enabled=True) # Grating_Start
        set_breakable(triggerIds=[6001], enabled=True) # Grating_Start
        set_breakable(triggerIds=[6002], enabled=True) # Grating_Start
        set_breakable(triggerIds=[6003], enabled=True) # Grating_Start
        set_breakable(triggerIds=[6004], enabled=True) # Grating_Start
        set_breakable(triggerIds=[6005], enabled=True) # Grating_Start
        set_breakable(triggerIds=[6006], enabled=True) # Grating_Start
        set_breakable(triggerIds=[6007], enabled=True) # Grating_Start
        set_breakable(triggerIds=[6008], enabled=True) # Grating_Start
        set_breakable(triggerIds=[6009], enabled=True) # Grating_Start
        set_breakable(triggerIds=[6010], enabled=True) # Grating_Start
        set_breakable(triggerIds=[6011], enabled=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6000], arg2=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6001], arg2=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6002], arg2=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6003], arg2=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6004], arg2=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6005], arg2=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6006], arg2=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6007], arg2=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6008], arg2=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6009], arg2=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6010], arg2=True) # Grating_Start
        set_visible_breakable_object(triggerIds=[6011], arg2=True) # Grating_Start

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BlockIng()


class BlockIng(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3901], visible=True, arg3=0, arg4=0, arg5=0) # InvisibleBarrier_TOKfalse
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return BlockEnd()


class BlockEnd(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6200,6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211], visible=True, arg3=0, arg4=0, arg5=0) # GratingDown
        set_breakable(triggerIds=[6000], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6001], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6002], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6003], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6004], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6005], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6006], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6007], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6008], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6009], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6010], enabled=False) # Grating_Start
        set_breakable(triggerIds=[6011], enabled=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6000], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6001], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6002], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6003], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6004], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6005], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6006], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6007], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6008], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6009], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6010], arg2=False) # Grating_Start
        set_visible_breakable_object(triggerIds=[6011], arg2=False) # Grating_Start

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BlockDisable()


class BlockDisable(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002105], state=1) # Lever_BlockOff

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002105], arg2=0):
            return BlockOffStart()


class BlockOffStart(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6200,6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211], visible=False, arg3=100, arg4=0, arg5=2) # GratingDown
        set_breakable(triggerIds=[6100], enabled=True) # Grating_Off
        set_breakable(triggerIds=[6101], enabled=True) # Grating_Off
        set_breakable(triggerIds=[6102], enabled=True) # Grating_Off
        set_breakable(triggerIds=[6103], enabled=True) # Grating_Off
        set_breakable(triggerIds=[6104], enabled=True) # Grating_Off
        set_breakable(triggerIds=[6105], enabled=True) # Grating_Off
        set_breakable(triggerIds=[6106], enabled=True) # Grating_Off
        set_breakable(triggerIds=[6107], enabled=True) # Grating_Off
        set_breakable(triggerIds=[6108], enabled=True) # Grating_Off
        set_breakable(triggerIds=[6109], enabled=True) # Grating_Off
        set_breakable(triggerIds=[6110], enabled=True) # Grating_Off
        set_breakable(triggerIds=[6111], enabled=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6100], arg2=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6101], arg2=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6102], arg2=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6103], arg2=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6104], arg2=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6105], arg2=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6106], arg2=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6107], arg2=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6108], arg2=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6109], arg2=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6110], arg2=True) # Grating_Off
        set_visible_breakable_object(triggerIds=[6111], arg2=True) # Grating_Off

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BlockOffIng()


class BlockOffIng(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3901], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleBarrier_TOKfalse
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return BlockOffEnd()


class BlockOffEnd(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6300,6301,6302,6303,6304,6305], visible=True, arg3=0, arg4=0, arg5=0) # GratingUp
        set_breakable(triggerIds=[6100], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6101], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6102], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6103], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6104], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6105], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6106], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6107], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6108], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6109], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6110], enabled=False) # Grating_Off
        set_breakable(triggerIds=[6111], enabled=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6100], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6101], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6102], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6103], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6104], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6105], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6106], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6107], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6108], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6109], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6110], arg2=False) # Grating_Off
        set_visible_breakable_object(triggerIds=[6111], arg2=False) # Grating_Off

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BlockEnable()


