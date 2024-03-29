""" trigger/02000382_bf/03_boss03portal.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=40, visible=False, enable=False, minimapVisible=False) # Boss01Spawn

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9900, spawnIds=[903]):
            return ActionPortal01(self.ctx)


class ActionPortal01(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=40, visible=False, enable=True, minimapVisible=False) # Boss01Spawn


initial_state = Wait
