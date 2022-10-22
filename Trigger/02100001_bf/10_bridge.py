""" trigger/02100001_bf/10_bridge.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3700,3701], visible=False, arg3=0, arg4=0, arg5=0) # Bridge Mesh

    def on_tick(self) -> state.State:
        if all_of():
            return BridgeOn()


class BridgeOn(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3700,3701], visible=True, arg3=300, arg4=0, arg5=2) # Bridge Mesh

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return BridgeOff()


class BridgeOff(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3700,3701], visible=False, arg3=0, arg4=0, arg5=2) # Bridge Mesh

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


