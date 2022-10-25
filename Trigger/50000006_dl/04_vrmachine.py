""" trigger/50000006_dl/04_vrmachine.xml """
import common


# 제논 시스템 연구소 : VR머신
class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='machineon', value=0)
        self.set_interact_object(triggerIds=[10001247], state=2)
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='machineon', value=1):
            return MachineOn(self.ctx)


class MachineOn(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001247], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001247], stateValue=0):
            return PortalOn(self.ctx)


class PortalOn(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ResetDelay(self.ctx)


class ResetDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10001247], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001247], stateValue=0):
            return PortalOn(self.ctx)


initial_state = Wait
