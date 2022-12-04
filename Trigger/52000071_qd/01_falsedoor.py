""" trigger/52000071_qd/01_falsedoor.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=0) # 미니맵용_Invisible
        self.set_interact_object(triggerIds=[10001103], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001103], stateValue=0):
            return MobSpawn(self.ctx)


class MobSpawn(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901], animationEffect=True)


initial_state = Wait
