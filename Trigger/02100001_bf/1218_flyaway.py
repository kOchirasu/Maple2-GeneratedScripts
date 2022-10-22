""" trigger/02100001_bf/1218_flyaway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='FlyAway', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FlyAway', value=1):
            return FlyAway()


class FlyAway(state.State):
    def on_enter(self):
        change_monster(removeSpawnId=218, addSpawnId=1218)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1218])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


