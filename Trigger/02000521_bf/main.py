""" trigger/02000521_bf/main.xml """
import common


class ready(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6001], visible=False)
        self.set_mesh(triggerIds=[6002], visible=False)
        self.set_mesh(triggerIds=[6003], visible=False)
        self.set_mesh(triggerIds=[6004], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[702]):
            return chaos_raid(self.ctx)


class chaos_raid(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[402], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ExitPortal', value=1):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.dungeon_clear()
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)


initial_state = ready
