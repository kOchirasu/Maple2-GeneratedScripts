""" trigger/52000071_qd/03_truedoor.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0) # 미니맵용_Invisible
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10001105], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001105], stateValue=0):
            return MobSpawn(self.ctx)


class MobSpawn(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True)


initial_state = Wait
