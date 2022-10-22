""" trigger/02100001_bf/213_mobspawn.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='RemoveAll', value=0)
        destroy_monster(spawnIds=[213])

    def on_tick(self) -> state.State:
        if check_user():
            return MobSpawn()


class MobSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[213], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[213]):
            return Delay01()
        if user_value(key='RemoveAll', value=1):
            return Quit()


class Delay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=40000):
            return MobSpawn()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[213])


