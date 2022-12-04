""" trigger/50000006_dl/03_vrmachine.xml """
import trigger_api


# 제논 시스템 연구소 : VR머신
class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='machineon', value=0)
        self.set_interact_object(triggerIds=[10001246], state=2)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='machineon', value=1):
            return MachineOn(self.ctx)


class MachineOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001246], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001246], stateValue=0):
            return PortalOn(self.ctx)


class PortalOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1, key='DungeonRoomOpened', value=1)
        self.set_portal(portalId=3, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ResetDelay(self.ctx)


class ResetDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10001246], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001246], stateValue=0):
            return PortalOn(self.ctx)


initial_state = Wait
