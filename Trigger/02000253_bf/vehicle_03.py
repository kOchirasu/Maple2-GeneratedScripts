""" trigger/02000253_bf/vehicle_03.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8053], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_max_user_count(value=3):
            return vehicle_01(self.ctx)


class vehicle_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=906, boxId=1):
            return monster_spawn_ready(self.ctx)


class monster_spawn_ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return monster_spawn(self.ctx)


class monster_spawn(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8053], visible=True)
        self.create_monster(spawnIds=[3001], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3001]):
            return vehicle_spawn(self.ctx)


class vehicle_spawn(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8053], visible=True)
        self.set_interact_object(triggerIds=[10001052], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001052], stateValue=0):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001052], state=2)


initial_state = idle
