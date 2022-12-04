""" trigger/02000452_bf/02_boss01portal.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=30, visible=False, enable=False, minimapVisible=False) # Boss01Spawn

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9900, spawnIds=[901]):
            return ActionPortal01(self.ctx)


class ActionPortal01(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=30, visible=False, enable=True, minimapVisible=False) # Boss01Spawn


initial_state = Wait
