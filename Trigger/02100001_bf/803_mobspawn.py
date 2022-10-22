""" trigger/02100001_bf/803_mobspawn.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='RemoveAll', value=0)
        destroy_monster(spawnIds=[803])
        set_mesh(triggerIds=[3203], visible=False, arg3=0, arg4=0, arg5=0) # Egg

    def on_tick(self) -> state.State:
        if check_user():
            return MobSpawn()


class MobSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[803], arg2=False)
        set_mesh(triggerIds=[3203], visible=True, arg3=0, arg4=0, arg5=0) # Egg

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[803]):
            return Delay01()
        if user_value(key='RemoveAll', value=1):
            return Quit()


class Delay01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3203], visible=False, arg3=0, arg4=0, arg5=0) # Egg

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=180000):
            return MobSpawn()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[803])


