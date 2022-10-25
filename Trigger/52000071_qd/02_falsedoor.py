""" trigger/52000071_qd/02_falsedoor.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0) # 미니맵용_Invisible
        self.set_interact_object(triggerIds=[10001104], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001104], stateValue=0):
            return MobSpawn(self.ctx)


class MobSpawn(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[902], animationEffect=True)


initial_state = Wait
