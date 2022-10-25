""" trigger/02000253_bf/vehicle_04.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8054], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_max_user_count(value=4):
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
        self.set_effect(triggerIds=[8054], visible=True)
        self.create_monster(spawnIds=[3002], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3002]):
            return vehicle_spawn(self.ctx)


class vehicle_spawn(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8054], visible=False)
        self.set_interact_object(triggerIds=[10001051], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001051], stateValue=0):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001051], state=2)


initial_state = idle
