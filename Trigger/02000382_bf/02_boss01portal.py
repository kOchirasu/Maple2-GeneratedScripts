""" trigger/02000382_bf/02_boss01portal.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=30, visible=False, enable=False, minimap_visible=False) # Boss01Spawn

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9900, spawn_ids=[901]):
            # 유저가 오른쪽에서 입장
            return ActionPortal01(self.ctx)


class ActionPortal01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=30, visible=False, enable=True, minimap_visible=False) # Boss01Spawn


initial_state = Wait
