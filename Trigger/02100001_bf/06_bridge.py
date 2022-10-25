""" trigger/02100001_bf/06_bridge.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3300,3301,3302], visible=False, arg3=0, delay=0, scale=0) # Bridge Mesh

    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return BridgeOn(self.ctx)


class BridgeOn(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3300,3301,3302], visible=True, arg3=300, delay=0, scale=2) # Bridge Mesh

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return BridgeOff(self.ctx)


class BridgeOff(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3300,3301,3302], visible=False, arg3=0, delay=0, scale=2) # Bridge Mesh

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
