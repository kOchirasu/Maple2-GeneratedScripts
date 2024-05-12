""" trigger/50000006_dl/04_vrmachine.xml """
import trigger_api


# 제논 시스템 연구소 : VR머신
class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='machineon', value=0)
        self.set_interact_object(trigger_ids=[10001247], state=2)
        self.set_portal(portal_id=4, visible=False, enable=False, minimap_visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='machineon', value=1):
            return MachineOn(self.ctx)


class MachineOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001247], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001247], state=0):
            return PortalOn(self.ctx)


class PortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4, visible=False, enable=True, minimap_visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ResetDelay(self.ctx)


class ResetDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4, visible=False, enable=False, minimap_visible=False)
        self.set_interact_object(trigger_ids=[10001247], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001247], state=0):
            return PortalOn(self.ctx)


initial_state = Wait
