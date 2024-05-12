""" trigger/52000071_qd/01_falsedoor.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], visible=False, start_delay=0, interval=0, fade=0) # 미니맵용_Invisible
        self.set_interact_object(trigger_ids=[10001103], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001103], state=0):
            return MobSpawn(self.ctx)


class MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901], auto_target=True)


initial_state = Wait
