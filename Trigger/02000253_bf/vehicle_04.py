""" trigger/02000253_bf/vehicle_04.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8054], visible=False)

    def on_tick(self) -> state.State:
        if dungeon_max_user_count(value=4):
            return vehicle_01()


class vehicle_01(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=906, boxId=1):
            return monster_spawn_ready()


class monster_spawn_ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return monster_spawn()


class monster_spawn(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8054], visible=True)
        create_monster(spawnIds=[3002], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3002]):
            return vehicle_spawn()


class vehicle_spawn(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8054], visible=False)
        set_interact_object(triggerIds=[10001051], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001051], arg2=0):
            return end()


class end(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001051], state=2)


