""" trigger/02000253_bf/vehicle_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8053], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_max_user_count(value=3):
            # 던전 최대 인원수가 3이면
            return vehicle_01(self.ctx)


class vehicle_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=906, min_users='1'):
            return monster_spawn_ready(self.ctx)


class monster_spawn_ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return monster_spawn(self.ctx)


class monster_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8053], visible=True)
        self.spawn_monster(spawn_ids=[3001], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3001]):
            return vehicle_spawn(self.ctx)


class vehicle_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8053], visible=True)
        self.set_interact_object(trigger_ids=[10001052], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001052], state=0):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001052], state=2)


initial_state = idle
