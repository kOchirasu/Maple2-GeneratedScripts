""" trigger/02100001_bf/08_bridge.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3500,3501], visible=False, arg3=0, delay=0, scale=0) # Bridge Mesh

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9500]) and self.user_detected(boxIds=[9501]):
            return BridgeOn(self.ctx)


class BridgeOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3500,3501], visible=True, arg3=300, delay=0, scale=2) # Bridge Mesh

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return BridgeOff(self.ctx)


class BridgeOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3500,3501], visible=False, arg3=0, delay=0, scale=2) # Bridge Mesh

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
